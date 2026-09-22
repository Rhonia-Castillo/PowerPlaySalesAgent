from __future__ import annotations

from datetime import datetime
import re
from pathlib import Path

import streamlit as st


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CONSTITUTION_PATH = REPOSITORY_ROOT / ".specify" / "memory" / "constitution.md"
SPECS_ROOT = REPOSITORY_ROOT / "specs"
DOCUMENTS = {
    "Specification": "spec.md",
    "Plan": "plan.md",
    "Tasks": "tasks.md",
    "Quality Checks": "checklists/requirements.md",
}
SECTION_NAMES = ("Overview", "Specification", "Plan", "Tasks", "Project Principles", "Quality Checks")
EXPECTED_FEATURE_FILES = tuple(DOCUMENTS.values())


def is_markdown_file(path: Path) -> bool:
    """Allow only Markdown files that remain inside the repository."""
    if path.suffix.lower() != ".md" or not path.is_file():
        return False
    try:
        path.resolve().relative_to(REPOSITORY_ROOT)
    except ValueError:
        return False
    return True


def discover_markdown_files() -> list[Path]:
    paths: list[Path] = []
    if is_markdown_file(CONSTITUTION_PATH):
        paths.append(CONSTITUTION_PATH)
    if SPECS_ROOT.is_dir():
        paths.extend(path for path in SPECS_ROOT.rglob("*.md") if is_markdown_file(path))
    return sorted(set(paths), key=lambda path: path.relative_to(REPOSITORY_ROOT).as_posix().lower())


def relative_path(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def active_feature_directory() -> Path | None:
    feature_file = REPOSITORY_ROOT / ".specify" / "feature.json"
    if not feature_file.is_file():
        return None
    try:
        import json

        feature_directory = json.loads(feature_file.read_text(encoding="utf-8"))["feature_directory"]
        path = (REPOSITORY_ROOT / feature_directory).resolve()
    except (OSError, KeyError, TypeError, ValueError):
        return None
    return path if path.is_dir() and path.is_relative_to(SPECS_ROOT.resolve()) else None


def file_metadata(path: Path) -> str:
    modified = datetime.fromtimestamp(path.stat().st_mtime).astimezone()
    return f"{relative_path(path)} | Last modified: {modified:%Y-%m-%d %H:%M:%S %Z}"


def feature_directories() -> list[Path]:
    if not SPECS_ROOT.is_dir():
        return []
    return sorted((path for path in SPECS_ROOT.iterdir() if path.is_dir()), key=lambda path: path.name.lower())


def feature_label(path: Path) -> str:
    return path.name


def document_path(feature_directory: Path, section: str) -> Path | None:
    if section == "Project Principles":
        return CONSTITUTION_PATH if is_markdown_file(CONSTITUTION_PATH) else None
    path = feature_directory / DOCUMENTS[section]
    return path if is_markdown_file(path) else None


def markdown_headings(content: str) -> list[tuple[int, str]]:
    return [(len(match.group("marks")), match.group("title").strip()) for match in re.finditer(
        r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*#*\s*$", content, re.MULTILINE
    )]


def heading_slug(title: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).strip().replace(" ", "-")


def render_toc(content: str) -> None:
    headings = markdown_headings(content)
    if not headings:
        return
    with st.expander("On this page", expanded=True):
        for level, title in headings:
            indent = "  " * max(level - 1, 0)
            st.markdown(f"{indent}- [{title}](#{heading_slug(title)})")


def search_content(feature_directory: Path, query: str) -> list[tuple[str, int, str]]:
    if not query.strip():
        return []
    matches: list[tuple[str, int, str]] = []
    for section, relative_file in DOCUMENTS.items():
        path = feature_directory / relative_file
        if not is_markdown_file(path):
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if query.casefold() in line.casefold():
                matches.append((section, line_number, line.strip()))
    return matches


def missing_feature_files() -> dict[str, list[str]]:
    missing: dict[str, list[str]] = {}
    if not SPECS_ROOT.is_dir():
        return missing
    for feature_dir in sorted(path for path in SPECS_ROOT.iterdir() if path.is_dir()):
        absent = [name for name in EXPECTED_FEATURE_FILES if not is_markdown_file(feature_dir / name)]
        if absent:
            missing[feature_dir.name] = absent
    return missing


def render_missing_files(feature_directory: Path) -> None:
    missing = [relative_file for relative_file in EXPECTED_FEATURE_FILES if not is_markdown_file(feature_directory / relative_file)]
    if missing:
        st.info("Not generated yet: " + ", ".join(missing))


def render_overview(feature_directory: Path) -> None:
    spec_path = feature_directory / "spec.md"
    if not is_markdown_file(spec_path):
        st.warning("The active feature has no spec.md yet.")
        return
    content = spec_path.read_text(encoding="utf-8", errors="replace")
    st.subheader("Feature overview")
    input_line = next((line.split("User description:", 1)[1].strip().strip('"')
                       for line in content.splitlines() if line.startswith("**Input**:") and "User description:" in line), "")
    status_line = next((line.split(":", 1)[1].strip() for line in content.splitlines() if line.startswith("**Status**:")), "Not stated")
    stage = "Specification created"
    if is_markdown_file(feature_directory / "tasks.md"):
        stage = "Tasks generated"
    elif is_markdown_file(feature_directory / "plan.md"):
        stage = "Plan generated"
    st.markdown(f"**Goal**  \n{input_line or 'Not stated in spec.md'}")
    st.markdown(f"**Current stage**: {stage}  \n**Spec status**: {status_line}")
    st.caption(file_metadata(spec_path))
    st.markdown("### Main sections")
    st.markdown("Open a complete source document. The viewer does not generate summaries or replace requirements.")
    for section in ("Specification", "Plan", "Tasks", "Project Principles", "Quality Checks"):
        if st.button(f"Open {section}", key=f"overview_{section}"):
            st.session_state["workspace_section"] = section
            st.rerun()
    render_missing_files(feature_directory)


def render_search_results(feature_directory: Path, query: str) -> None:
    matches = search_content(feature_directory, query)
    if not query.strip():
        return
    st.sidebar.caption(f"{len(matches)} match(es)")
    if not matches:
        st.info(f'No matches for "{query}" in this feature.')
        return
    with st.expander("Search matches", expanded=True):
        for section, line_number, line in matches[:100]:
            st.markdown(f"**{section}, line {line_number}**")
            st.code(line or "(blank line)", language="markdown")


def main() -> None:
    st.set_page_config(page_title="PowerPlay Sales Expert | Spec Workspace", page_icon="📚", layout="wide")
    st.markdown("""
    <style>
    .block-container { max-width: 1180px; padding-top: 2rem; }
    [data-testid="stMarkdownContainer"] { line-height: 1.65; }
    [data-testid="stMarkdownContainer"] pre { max-width: 100%; overflow-x: auto; }
    </style>
    """, unsafe_allow_html=True)

    if st.sidebar.button("Refresh", type="primary", use_container_width=True):
        st.rerun()

    features = feature_directories()
    if not features:
        st.warning("No Spec Kit feature directories were found under specs/.")
        return

    active_feature = active_feature_directory()
    default_index = features.index(active_feature) if active_feature in features else 0
    selected_feature = st.sidebar.selectbox("Feature", features, index=default_index, format_func=feature_label)
    selected_section = st.sidebar.radio("Workspace", SECTION_NAMES, index=0, key="workspace_section")
    query = st.sidebar.text_input("Search current feature", placeholder="Search requirements, risks, or headings")

    st.title("PowerPlay Sales Expert")
    st.caption(f"Developer specification workspace | {selected_feature.name}")

    if selected_section == "Overview":
        render_overview(selected_feature)
    else:
        selected_path = document_path(selected_feature, selected_section)
        if selected_path is None:
            expected_path = relative_path(CONSTITUTION_PATH if selected_section == "Project Principles" else selected_feature / DOCUMENTS[selected_section])
            st.subheader(selected_section)
            st.info(f"Not generated yet: {expected_path}")
            st.caption("This view will appear automatically after the source Markdown file is created.")
        else:
            st.subheader(selected_section)
            st.caption(file_metadata(selected_path))
            content = selected_path.read_text(encoding="utf-8", errors="replace")
            render_toc(content)
            st.markdown(content)

    render_search_results(selected_feature, query)


if __name__ == "__main__":
    main()
