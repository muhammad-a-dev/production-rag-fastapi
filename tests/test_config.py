"""Unit tests for settings helpers."""

from pathlib import Path

from rag.config import Settings


def test_chroma_path_is_absolute_under_project_root() -> None:
    settings = Settings(chroma_persist_directory="chroma_db")
    assert settings.chroma_path.is_absolute()
    assert settings.chroma_path.name == "chroma_db"
    assert settings.project_root in settings.chroma_path.parents


def test_temp_path_respects_absolute_override(tmp_path: Path) -> None:
    settings = Settings(temp_upload_dir=str(tmp_path))
    assert settings.temp_path == tmp_path


def test_chroma_path_respects_absolute_override(tmp_path: Path) -> None:
    settings = Settings(chroma_persist_directory=str(tmp_path))
    assert settings.chroma_path == tmp_path


def test_numeric_knobs_coerce_from_strings() -> None:
    """Env vars arrive as strings; Settings should coerce chunk/retriever knobs."""
    settings = Settings(
        chunk_size="750",
        chunk_overlap="75",
        retriever_k="5",
        retriever_score_threshold="0.35",
    )
    assert settings.chunk_size == 750
    assert settings.chunk_overlap == 75
    assert settings.retriever_k == 5
    assert settings.retriever_score_threshold == 0.35
