from pydays import editor


def _fake_which(available):
    return lambda name: f"/usr/bin/{name}" if name in available else None


def test_vim_is_default(monkeypatch):
    monkeypatch.delenv("PYDAYS_EDITOR", raising=False)
    monkeypatch.setenv("EDITOR", "nano")          # ignored: vim is the editor
    monkeypatch.setattr(editor.shutil, "which", _fake_which({"vim", "nano"}))
    cmd = editor.find_editor()
    assert cmd[0] == "vim" and editor.VIM_SETTINGS in cmd and editor.uses_vim()


def test_falls_back_to_vi_then_none(monkeypatch):
    monkeypatch.delenv("PYDAYS_EDITOR", raising=False)
    monkeypatch.setattr(editor.shutil, "which", _fake_which({"vi"}))
    assert editor.find_editor() == ["vi"]
    monkeypatch.setattr(editor.shutil, "which", _fake_which(set()))
    assert editor.find_editor() is None and not editor.uses_vim()


def test_override(monkeypatch):
    monkeypatch.setenv("PYDAYS_EDITOR", "code --wait")
    assert editor.find_editor() == ["code", "--wait"] and not editor.uses_vim()


def test_paste_mode():
    lines = iter(["a = 1", "print(a)", "END", "ignored"])
    assert editor.paste_code(lambda: next(lines)) == "a = 1\nprint(a)\n"
