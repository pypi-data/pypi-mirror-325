import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import asyncpg  # type: ignore [import-untyped]
import httpx
from httpx import Response
from pydantic import BaseModel

from chatwoot_api.settings import settings

logger = logging.getLogger(__name__)


class Sender(BaseModel):  # TODO: is the same of OuterSender?
    id: int
    name: str
    available_name: str | None = None
    avatar_url: str | None = None
    type: str
    availability_status: str | None = None
    thumbnail: str | None = None
    additional_attributes: dict | None = None
    custom_attributes: dict | None = None
    email: str | None = None
    identifier: Any | None = None
    phone_number: str | None = None


class MessageData(BaseModel):
    id: int
    content: str
    inbox_id: int
    conversation_id: int
    message_type: int
    content_type: str
    status: str
    content_attributes: dict
    created_at: int
    private: bool
    source_id: str | int | None = None
    sender: Sender | None = None


class Team(BaseModel):
    id: int
    name: str
    description: str


class Account(BaseModel):
    id: int
    name: str


class ContactInbox(BaseModel):
    id: int
    contact_id: int
    inbox_id: int
    source_id: str
    created_at: datetime
    updated_at: datetime
    hmac_verified: bool
    pubsub_token: str


class ConversationContactInbox(BaseModel):
    source_id: str


class MessageConversationNested(BaseModel):
    assignee_id: int | None = None
    unread_count: int
    last_activity_at: int
    contact_inbox: ConversationContactInbox


class Message(BaseModel):
    id: int
    content: str
    inbox_id: int
    conversation_id: int
    message_type: int
    content_type: str
    status: str
    content_attributes: dict
    created_at: int  # UNIX timestamp
    private: bool
    source_id: str | int | None = None
    sender: Sender | None = None
    account_id: int | None = None
    updated_at: datetime | None = None
    sender_type: str | None = None
    sender_id: int | None = None
    external_source_ids: dict | None = None
    additional_attributes: dict | None = None
    processed_message_content: str | None = None
    sentiment: dict | None = None
    conversation: MessageConversationNested | None = None


class Meta(BaseModel):
    sender: Sender | None = None
    assignee: Any | None = None
    team: Any | None = None
    hmac_verified: bool | None = None
    labels: list | None = None
    additional_attributes: dict | None = None
    contact: Sender | None = None
    agent_last_seen_at: str | None = None
    assignee_last_seen_at: str | None = None


class Conversation(BaseModel):
    additional_attributes: dict
    agent_last_seen_at: int
    can_reply: bool
    channel: str
    contact_inbox: ContactInbox
    contact_last_seen_at: int
    created_at: int
    custom_attributes: dict
    first_reply_created_at: Any | None = None
    id: int
    inbox_id: int
    labels: list
    last_activity_at: int
    messages: list
    meta: Meta
    priority: Any | None = None
    snoozed_until: Any | None = None
    status: str
    timestamp: int
    unread_count: int
    waiting_since: int


class Inbox(BaseModel):
    id: int
    name: str


class OuterSender(BaseModel):  # TODO: is the same of Sender?
    account: Account | None = None
    additional_attributes: dict | None = None
    avatar: str | None = None
    custom_attributes: dict | None = None
    email: str | None = None
    id: int
    identifier: Any | None = None
    name: str
    phone_number: str | None = None
    thumbnail: str | None = None


class MessageCreatedEvent(BaseModel):
    account: Account
    additional_attributes: dict
    content_attributes: dict
    content_type: str
    content: str | None = None
    conversation: Conversation
    created_at: datetime
    id: int
    inbox: Inbox
    message_type: str
    private: bool
    sender: OuterSender
    source_id: str | int | None = None
    event: str


class ResponseModel(BaseModel):
    meta: Meta
    payload: list[Message]


def print_response(response: Response) -> None:
    logger.info(response.status_code)
    try:
        logger.info(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except:
        logger.info(response.text)


def get_query(name: str) -> str:
    system_file_path = Path(__file__).parent / "sql" / f"{name}.sql"
    with system_file_path.open(encoding="utf-8") as system_file:
        return system_file.read()


async def get_api_access_token(account_id: int) -> str:
    conn = await asyncpg.connect(
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
    )
    values = await conn.fetch(
        get_query("get_user_token"),
        account_id,
    )
    await conn.close()
    return str(values[0]["token"])


def get_chat_history(
    api_access_token: str,
    account_id: int,
    conversation_id: int,
) -> list[str]:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_access_token": f"{api_access_token}",
    }
    url = f"{settings.chatwoot_base_url}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    response = httpx.get(url, headers=headers)
    messages: list[dict[str, Any]] = response.json()
    print_response(response)
    payload = ResponseModel.model_validate(messages).payload
    message_list = [message.content for message in payload]
    message_list.pop()
    return message_list


def get_teams_list(api_access_token: str, account_id: int) -> list[Team]:
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "api_access_token": f"{api_access_token}",
    }
    url = f"{settings.chatwoot_base_url}/api/v1/accounts/{account_id}/teams"
    response = httpx.get(url, headers=headers)
    print_response(response)
    teams: list[dict[str, Any]] = response.json()
    return [Team.model_validate(team) for team in teams]


def assign_conversation_to_team(
    api_access_token: str,
    team_id: int,
    account_id: int,
    conversation_id: int,
) -> None:
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "api_access_token": f"{api_access_token}",
    }
    body = {"assignee_id": None, "team_id": team_id}
    url = f"{settings.chatwoot_base_url}/api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments"
    response = httpx.post(url, headers=headers, json=body)
    print_response(response)


def update_conversation_status(
    api_access_token: str,
    account_id: int,
    conversation_id: int,
) -> None:
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "api_access_token": f"{api_access_token}",
    }
    url = f"{settings.chatwoot_base_url}/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status"
    body = {"status": "open"}
    response = httpx.post(url, headers=headers, json=body)
    print_response(response)


def send_conversation_response(
    api_access_token: str,
    account: int,
    conversation: int,
    message: str,
) -> MessageData:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_access_token": f"{api_access_token}",
    }
    data = {"content": message}
    url = f"{settings.chatwoot_base_url}/api/v1/accounts/{account}/conversations/{conversation}/messages"
    response = httpx.post(url, json=data, headers=headers)
    print_response(response)
    return MessageData.model_validate(response.json())
