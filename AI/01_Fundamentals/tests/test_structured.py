
from pydantic import BaseModel

class Answer(BaseModel):
    content: str
    citations: list

def test_schema_validate():
    raw = '{"content": "hello", "citations": ["1"]}'
    parsed = Answer.model_validate_json(raw)
    assert parsed.content == "hello"
    assert parsed.citations == ["1"]

def test_schema_strict():
    try:
        Answer.model_validate_json('{"content": "hello"}')  # missing citations
        assert False, "should have raised"
    except Exception:
        pass  # expected validation error
