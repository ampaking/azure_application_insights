# Python FastAPI アプリケーションにおける Azure Application Insights を利用した高度な監視機能の実装

現代のソフトウェア開発において、監視機能はアプリケーションの状態をモニタリングし、問題を積極的に解決するための基石です。
この記事では、Python FastAPI アプリケーションと Azure Application Insights の統合プロセスを簡略化し、初心者を含む開発者が効果的に高度な監視ソリューションを実装できるようにするセットアップに焦点を当てます。

## シームレスな統合のための前提条件

Python アプリケーションに Azure Application Insights を統合する前に、以下のものを準備しておく必要があります：

- Azure のサブスクリプション。
- Python アプリケーション用に作成された App Service・など。
- Python 3.7 以上。

## Azure Application Insights の設定

最初のステップは、Azure Application Insights リソースを設定することです。このプロセスでは、統合に不可欠な接続文字列を提供します。この接続文字列を安全に保管してください。アプリケーションを設定するために必要になります。

## 必要なパッケージのインストール

pip を使用して azure-monitor-opentelemetry、pip install opentelemetry-instrumentation-fastapi 　パッケージをインストールし、プロジェクトの依存関係を効率的に管理するために requirements.txt ファイルに追加します。

```
pip install azure-monitor-opentelemetry
pip install opentelemetry-instrumentation-fastapi
```

## 設定

設定管理は非常に重要です。Azure Application Insights の接続文字列を環境変数に保存して、安全かつ柔軟にアクセスできるようにします。アプリケーションでこの設定を強制する方法は次のとおりです：

```
import os
import logging

from fastapi import FastAPI, HTTPException
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from dotenv import load_dotenv

# Load environment variable
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

app = FastAPI()

APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv(
    "APPLICATIONINSIGHTS_CONNECTION_STRING"
)

# Simple validation
assert (
    APPLICATIONINSIGHTS_CONNECTION_STRING
), "APPLICATIONINSIGHTS_CONNECTION_STRING is not set."


try:
    configure_azure_monitor(
        connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING,
    )
    FastAPIInstrumentor.instrument_app(app)
except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=f"Application Insights was not set up properly. {(str(e))}",
    ) from e


@app.get("/health_check")
async def health_check():
    """
    The `health_check` function in Python implements custom logic for performing a health check and
    returns a dictionary with a status message.
    :return: The `health_check` function is returning a dictionary with a key "status" and the value "I
    am ok!!!".
    """

    logger.info("Health check endpoint was called")

    return {"status": "I am ok!!!"}
```

このシンプルなエンドポイントは、アプリケーションが実行中でリクエストを処理できることを確認するためのヘルスチェックとして機能します。このようなエンドポイントを組み込むことは、アプリケーションの信頼性とパフォーマンスを維持するために重要です。

## まとめ

Python FastAPI アプリケーションと Azure Application Insights を統合することは、アプリケーションのパフォーマンスとユーザーエクスペリエンスに関する深い洞察を提供することで観測性を大幅に強化します。すべてのレベルの開発者を対象としたこのガイドは、この強力な監視ツールの設定の簡単さを示しています。これらのステップに従うことで、アプリケーションを堅牢で、パフォーマンスが高く、信頼できるものに保ち、卓越したユーザーエクスペリエンスを提供する能力を強化します。

Azure サービスを活用して Python アプリケーションを向上させるためのより深い記事にご期待ください。実践していただいた皆様のフィードバックは非常に価値がありますので、これらの実践を実装する際のご意見や経験を共有してください。
