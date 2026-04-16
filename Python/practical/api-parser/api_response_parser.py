import json
import requests
import time
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: Optional[str]


def parse_users(json_response: str) -> List[User]:
    """深くネストした JSON からユーザーリストを抽出（Null/空文字対応）"""
    try:
        data = json.loads(json_response)
    except json.JSONDecodeError:
        return []

    raw_users = (data.get("payload", {}).get("data", []))
    users: List[User] = []

    for u in raw_users:
        profile = u.get("profile") or {}
        contact = u.get("contact") or {}

        name = profile.get("name") or "Unknown"
        email = contact.get("email") or None

        users.append(
            User(
                id=u.get("id", 0),
                name=name,
                email=email
            )
        )

    return users


def fetch_users_with_retry(url: str, max_retries: int = 5) -> List[User]:
    """API取得＋ネストパース＋エラーハンドリング＋指数バックオフリトライ"""
    retry = 0

    while retry < max_retries:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return parse_users(response.text)

        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError) as e:

            wait = 2 ** retry
            print(f"Retry {retry + 1}/{max_retries} after {wait}s ... ({e})")
            time.sleep(wait)
            retry += 1

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            return []

        except Exception as e:
            print(f"Unknown error: {e}")
            return []

    print("Exceeded max retries")
    return []
