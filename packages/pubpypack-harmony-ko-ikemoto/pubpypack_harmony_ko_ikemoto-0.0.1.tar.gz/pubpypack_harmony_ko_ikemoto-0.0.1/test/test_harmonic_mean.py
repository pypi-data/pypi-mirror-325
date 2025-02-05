#import harmonic_mean
import imppkg.harmonic_mean
def test_always_passes():
    # このアサーションは常に成功する
    x = 1
    assert x > 0, "このアサーションは常に成功するはずだ"

import sys
from termcolor import colored
from imppkg.harmony import main

def test_harmony_happy_path(monkeypatch, capsys):
    # 入力値を設定
    inputs = ["1", "4", "4"]
    
    # sys.argv をモンキーパッチで置き換え
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    # main() を実行
    main()

    # 期待値を計算
    expected_value = 2.0

    # 標準出力の取得とアサーション
    assert capsys.readouterr().out.strip() == colored(
        expected_value,
        "red",
        "on_cyan",
        attrs=["bold"]
    )

def test_harmony_zero_division(monkeypatch, capsys):
    # 0 のみを入力
    monkeypatch.setattr(sys, "argv", ["harmony", "0"])
    
    main()
    
    # 0 の出力を確認
    assert capsys.readouterr().out.strip() == colored(
        0.0,
        "red",
        "on_cyan",
        attrs=["bold"]
    )

def test_harmony_value_error(monkeypatch, capsys):
    # 数値変換できない文字列を入力
    monkeypatch.setattr(sys, "argv", ["harmony", "abc", "def"])
    
    main()
    
    # 0 の出力を確認
    assert capsys.readouterr().out.strip() == colored(
        0.0,
        "red",
        "on_cyan",
        attrs=["bold"]
    )

