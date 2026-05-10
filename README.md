# Sample CI/CD Project

FastAPI を使用したシンプルな CI/CD 学習プロジェクトです。

## プロジェクト構成
sample-cicd-project/
├── app/
│   ├── init.py
│   └── main.py              # FastAPI アプリケーション
├── tests/
│   ├── init.py
│   └── test_main.py         # ユニットテスト
├── venv/                    # Python仮想環境
├── requirements.txt         # パッケージ一覧
├── .gitignore
└── README.md

## セットアップ方法

```bash
# 1. 仮想環境を作成
python3 -m venv venv

# 2. 仮想環境を有効化
source venv/bin/activate

# 3. パッケージをインストール
pip install -r requirements.txt
```

## テスト実行

```bash
# テストを実行
pytest tests/test_main.py -v

# 全テストを実行
pytest -v
```

## アプリケーション実行

```bash
# 開発サーバーを起動
uvicorn app.main:app --reload

# ブラウザでアクセス
# http://localhost:8000
# http://localhost:8000/docs (自動生成されたAPI仕様)
```

## エンドポイント

- `GET /` - ウェルカムメッセージ
- `GET /items/{item_id}` - アイテム取得
- `GET /health` - ヘルスチェック

## CI/CD パイプライン

このプロジェクトは以下の CI/CD パイプラインを構築しています：

1. **CI（継続的インテグレーション）**
   - GitHub Actions でテストを自動実行
   - コード品質チェック

2. **CD（継続的デリバリー）**
   - Vercel へ自動デプロイ

## 構築予定

- [x] FastAPI プロジェクト作成
- [x] ユニットテスト作成
- [ ] GitHub Actions 設定
- [ ] Vercel デプロイ設定
