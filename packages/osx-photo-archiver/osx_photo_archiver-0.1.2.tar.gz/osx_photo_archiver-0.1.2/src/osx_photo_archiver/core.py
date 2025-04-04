"""
OSX Photo Archiver Core Module
写真・動画を年/月ディレクトリに整理するコア機能を提供
"""
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, List

@dataclass
class ExportConfig:
    """エクスポート設定を保持するデータクラス"""
    output_dir: Path
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    skip_duplicates: bool = True

class PhotoArchiver:
    """写真アーカイブの主要機能を提供するクラス"""

    def __init__(self, config: ExportConfig):
        """
        Args:
            config (ExportConfig): エクスポート設定
        """
        self.config = config
        self._validate_config()

    def _validate_config(self) -> None:
        """設定の妥当性を検証"""
        if self.config.from_date and self.config.to_date:
            if self.config.from_date > self.config.to_date:
                raise ValueError("開始日が終了日より後になっています")

    def _build_export_command(self) -> List[str]:
        """osxphotosコマンドを構築"""
        cmd = [
            "osxphotos", "export",
            "--directory", "{created.year}/{created.mm}",
            "--filename", "{original_name}",
            str(self.config.output_dir)
        ]

        if self.config.from_date:
            cmd.extend(["--from-date", self.config.from_date.strftime("%Y-%m-%d")])

        if self.config.to_date:
            cmd.extend(["--to-date", self.config.to_date.strftime("%Y-%m-%d")])

        if self.config.skip_duplicates:
            cmd.append("--skip-duplicate")

        return cmd

    def export(self) -> None:
        """写真のエクスポートを実行"""
        import subprocess
        import shutil

        # osxphotosコマンドが利用可能か確認
        if not shutil.which("osxphotos"):
            raise RuntimeError(
                "osxphotosコマンドが見つかりません。"
                "'pip install osxphotos'を実行してインストールしてください。"
            )

        # 出力先ディレクトリが存在しない場合は作成
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

        # コマンドの構築と実行
        cmd = self._build_export_command()
        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            # 成功時のログ出力
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            # コマンド実行エラー時
            error_msg = f"エクスポート中にエラーが発生しました: {e.stderr}"
            print(error_msg, file=sys.stderr)
            raise RuntimeError(error_msg) from e
        except Exception as e:
            # その他の予期せぬエラー
            error_msg = f"予期せぬエラーが発生しました: {str(e)}"
            print(error_msg, file=sys.stderr)
            raise

    def verify_permissions(self) -> bool:
        """必要な権限が付与されているか確認"""
        import os
        import subprocess

        # 1. 親ディレクトリの存在確認
        if not self.config.output_dir.parent.exists():
            print(
                f"エラー: 親ディレクトリが存在しません: {self.config.output_dir.parent}",
                file=sys.stderr
            )
            return False

        # 2. 出力先ディレクトリの書き込み権限確認
        try:
            # 出力先ディレクトリが存在しない場合は作成を試みる
            self.config.output_dir.mkdir(parents=True, exist_ok=True)
            test_file = self.config.output_dir / ".permission_test"
            test_file.touch()
            test_file.unlink()
        except (PermissionError, OSError):
            print(
                f"エラー: 出力先ディレクトリ {self.config.output_dir} への書き込み権限がありません",
                file=sys.stderr
            )
            return False

        # 2. Photosライブラリへのアクセス確認
        try:
            # osxphotosの簡単なコマンドを実行してアクセス権限を確認
            subprocess.run(
                ["osxphotos", "list"],
                check=True,
                capture_output=True,
                text=True
            )
            return True
        except subprocess.CalledProcessError:
            print(
                "エラー: Photosライブラリへのアクセス権限がありません。\n"
                "システム環境設定 > プライバシーとセキュリティ > フルディスクアクセス で\n"
                "ターミナルまたはVSCodeに権限を付与してください。",
                file=sys.stderr
            )
            return False
        except FileNotFoundError:
            print(
                "エラー: osxphotosコマンドが見つかりません。\n"
                "'pip install osxphotos'を実行してインストールしてください。",
                file=sys.stderr
            )
            return False
