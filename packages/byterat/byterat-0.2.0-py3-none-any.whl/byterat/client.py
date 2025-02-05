import json
from enum import Enum
from typing import final

import pandas as pd
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.requests import RequestsHTTPTransport
from typing_extensions import override

from .config import BYTERAT_URL
from .queries import (
  GET_DATASET_CYCLE_DATA,
  GET_FILTERED_DATASET_CYCLE_DATA,
  GET_FILTERED_METADATA,
  GET_FILTERED_OBSERVATION_DATA,
  GET_METADATA,
  GET_OBSERVATION_DATA,
)


class ByteratData:
  def __init__(self, data: list[str], continuation_token: str | None) -> None:
    self.data: pd.DataFrame = pd.DataFrame([json.loads(entry) for entry in data])
    self.continuation_token: str | None = continuation_token


class ByteratOperator(Enum):
  LT = 'lt'
  LTE = 'lte'
  EQ = 'equals'
  GTE = 'gte'
  GT = 'gt'
  CONTAINS = 'contains'
  NOT = 'not'
  STARTS_WITH = 'startsWith'
  ENDS_WITH = 'endsWith'
  SEARCH = 'search'
  NOT_CONTAINS = 'notContains'
  IN = 'in'
  NOT_IN = 'notIn'
  IS_NULL = 'isNull'
  IS_NOT_NULL = 'isNotNull'
  HAS = 'has'
  HAS_EVERY = 'hasEvery'
  HAS_SOME = 'hasSome'


@final
class ByteratFilter:
  def __init__(
    self,
    column: str,
    operator: ByteratOperator,
    value: str | int,
    mode: str = 'default',
  ) -> None:
    if mode not in ['default', 'insensitive']:
      raise Exception("Invalid mode. Must be one of ['default', 'insensitive']")

    self.column = column
    self.operator = operator
    self.value = value
    self.mode = mode

  def to_dict(self) -> dict[str, str | int]:
    """
    Convert the filter to a dictionary format, which can be handy for serialization
    or sending as part of a GraphQL query.
    """
    data: dict[str, str | int] = {
      'column': self.column,
      'operator': self.operator.value,  # Use .value to get the underlying string
      'value': self.value,
      'mode': self.mode,
    }

    return data

  @override
  def __repr__(self) -> str:
    return (
      f'ByteratFilter(column={self.column}, operator={self.operator}, '
      f'value={self.value}, mode={self.mode})'
    )


def convert_byterat_filters(filters: list[ByteratFilter]) -> list[dict[str, str | int]]:
  return [filter_obj.to_dict() for filter_obj in filters]


class ByteratClientAsync:
  def __init__(self, token: str) -> None:
    self.token: str = token
    self.transport: AIOHTTPTransport = AIOHTTPTransport(
      BYTERAT_URL,
      headers={'workspace_api_key': token},
    )
    self.client: Client = Client(
      transport=self.transport, fetch_schema_from_transport=True
    )

  async def __get_observation_metrics(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
    dataset_cycle: int | None = None,
    file_name: str | None = None,
  ) -> ByteratData:
    query = gql(GET_OBSERVATION_DATA)

    variables: dict[str, str | int | None] = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    if dataset_cycle:
      variables['dataset_cycle'] = dataset_cycle

    if file_name:
      variables['file_name'] = file_name

    async with self.client as session:
      resp = await session.execute(query, variable_values=variables)

    data: list[str] = resp['get_observation_data_by_workspace']['data']
    continuation_token = resp['get_observation_data_by_workspace']['continuation_token']
    return ByteratData(data, continuation_token)

  async def get_observation_metrics(
    self, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_observation_metrics(continuation_token=continuation_token)

  async def get_observation_metrics_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_observation_metrics(
      dataset_key=dataset_key, continuation_token=continuation_token
    )

  async def get_observation_metrics_by_dataset_key_and_dataset_cycle(
    self, dataset_key: str, dataset_cycle: int, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_observation_metrics(
      dataset_key=dataset_key,
      dataset_cycle=dataset_cycle,
      continuation_token=continuation_token,
    )

  async def get_observation_metrics_by_filename(
    self, file_name: str, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_observation_metrics(
      file_name=file_name,
      continuation_token=continuation_token,
    )

  async def __get_metdata(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
  ) -> ByteratData:
    query = gql(GET_METADATA)
    variables = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    async with self.client as session:
      resp = await session.execute(query, variable_values=variables)

    data: list[str] = resp['get_metadata_by_workspace']['data']
    continuation_token = resp['get_metadata_by_workspace']['continuation_token']
    return ByteratData(data, continuation_token)

  async def get_metadata(self, continuation_token: str | None = None) -> ByteratData:
    return await self.__get_metdata(continuation_token=continuation_token)

  async def get_metadata_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_metdata(
      dataset_key=dataset_key, continuation_token=continuation_token
    )

  async def __get_dataset_cycle_metrics(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
    dataset_cycle: int | None = None,
    file_name: str | None = None,
  ) -> ByteratData:
    query = gql(GET_DATASET_CYCLE_DATA)

    variables: dict[str, str | int | None] = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    if dataset_cycle:
      variables['dataset_cycle'] = dataset_cycle

    if file_name:
      variables['file_name'] = file_name

    async with self.client as session:
      resp = await session.execute(query, variable_values=variables)

    data: list[str] = resp['get_dataset_cycle_data_by_workspace']['data']
    continuation_token = resp['get_dataset_cycle_data_by_workspace'][
      'continuation_token'
    ]
    return ByteratData(data, continuation_token)

  async def get_dataset_cycle_data(
    self, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_dataset_cycle_metrics(continuation_token=continuation_token)

  async def get_dataset_cycle_data_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_dataset_cycle_metrics(
      dataset_key=dataset_key, continuation_token=continuation_token
    )

  async def get_dataset_cycle_data_by_dataset_key_and_dataset_cycle(
    self, dataset_key: str, dataset_cycle: int, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_dataset_cycle_metrics(
      dataset_key=dataset_key,
      dataset_cycle=dataset_cycle,
      continuation_token=continuation_token,
    )

  async def get_dataset_cycle_data_by_filename(
    self, file_name: str, continuation_token: str | None = None
  ) -> ByteratData:
    return await self.__get_dataset_cycle_metrics(
      file_name=file_name,
      continuation_token=continuation_token,
    )


class ByteratClientSync:
  def __init__(self, token: str) -> None:
    self.token = token
    self.transport = RequestsHTTPTransport(
      url=BYTERAT_URL,
      headers={'workspace_api_key': token},
      verify=True,
      retries=3,
    )
    self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

  def __get_observation_metrics(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
    dataset_cycle: int | None = None,
    file_name: str | None = None,
  ) -> ByteratData:
    query = gql(GET_OBSERVATION_DATA)

    variables: dict[str, str | int | None] = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    if dataset_cycle:
      variables['dataset_cycle'] = dataset_cycle

    if file_name:
      variables['file_name'] = file_name

    resp = self.client.execute(query, variable_values=variables)

    data: list[str] = resp['get_observation_data_by_workspace']['data']
    continuation_token = resp['get_observation_data_by_workspace']['continuation_token']
    return ByteratData(data, continuation_token)

  def get_observation_metrics(
    self, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_observation_metrics(continuation_token=continuation_token)

  def get_observation_metrics_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_observation_metrics(
      continuation_token=continuation_token,
      dataset_key=dataset_key,
    )

  def get_observation_metrics_by_dataset_key_and_dataset_cycle(
    self, dataset_key: str, dataset_cycle: int, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_observation_metrics(
      continuation_token=continuation_token,
      dataset_key=dataset_key,
      dataset_cycle=dataset_cycle,
    )

  def get_observation_metrics_by_filename(
    self, file_name: str, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_observation_metrics(
      continuation_token=continuation_token,
      file_name=file_name,
    )

  def __get_dataset_cycle_metrics(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
    dataset_cycle: int | None = None,
    file_name: str | None = None,
  ) -> ByteratData:
    query = gql(GET_DATASET_CYCLE_DATA)

    variables: dict[str, str | int | None] = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    if dataset_cycle:
      variables['dataset_cycle'] = dataset_cycle

    if file_name:
      variables['file_name'] = file_name

    resp = self.client.execute(query, variable_values=variables)

    data: list[str] = resp['get_dataset_cycle_data_by_workspace']['data']
    continuation_token = resp['get_dataset_cycle_data_by_workspace'][
      'continuation_token'
    ]
    return ByteratData(data, continuation_token)

  def get_dataset_cycle_data(
    self, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_dataset_cycle_metrics(
      continuation_token=continuation_token,
    )

  def get_dataset_cycle_data_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_dataset_cycle_metrics(
      continuation_token=continuation_token,
      dataset_key=dataset_key,
    )

  def get_dataset_cycle_data_by_dataset_key_and_dataset_cycle(
    self, dataset_key: str, dataset_cycle: int, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_dataset_cycle_metrics(
      continuation_token=continuation_token,
      dataset_key=dataset_key,
      dataset_cycle=dataset_cycle,
    )

  def get_dataset_cycle_data_by_filename(
    self, file_name: str, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_dataset_cycle_metrics(
      continuation_token=continuation_token,
      file_name=file_name,
    )

  def __get_metadata(
    self,
    continuation_token: str | None = None,
    dataset_key: str | None = None,
  ) -> ByteratData:
    query = gql(GET_METADATA)
    variables = {'continuation_token': continuation_token}

    if dataset_key:
      variables['dataset_key'] = dataset_key

    resp = self.client.execute(query, variable_values=variables)

    data: list[str] = resp['get_metadata_by_workspace']['data']
    continuation_token = resp['get_metadata_by_workspace']['continuation_token']
    return ByteratData(data, continuation_token)

  def get_metadata(self, continuation_token: str | None = None) -> ByteratData:
    return self.__get_metadata(continuation_token=continuation_token)

  def get_metadata_by_dataset_key(
    self, dataset_key: str, continuation_token: str | None = None
  ) -> ByteratData:
    return self.__get_metadata(
      continuation_token=continuation_token, dataset_key=dataset_key
    )

  def __get_filtered_data(
    self,
    filters: list[ByteratFilter],
    query_info: dict[str, str] = GET_FILTERED_OBSERVATION_DATA,
    continuation_token: str | None = None,
  ):
    query = gql(query_info['query'])

    variables = {
      'continuation_token': continuation_token,
      'filters': convert_byterat_filters(filters),
    }

    resp = self.client.execute(query, variable_values=variables)

    data: list[str] = resp[query_info['endpoint']]['data']
    continuation_token = resp[query_info['endpoint']]['continuation_token']
    return ByteratData(data, continuation_token)

  def get_filtered_observation_data(
    self,
    filters: list[ByteratFilter],
    continuation_token: str | None = None,
  ) -> ByteratData:
    return self.__get_filtered_data(
      filters=filters,
      continuation_token=continuation_token,
      query_info=GET_FILTERED_OBSERVATION_DATA,
    )

  def get_filtered_dataset_cycle_data(
    self,
    filters: list[ByteratFilter],
    continuation_token: str | None = None,
  ) -> ByteratData:
    return self.__get_filtered_data(
      filters=filters,
      continuation_token=continuation_token,
      query_info=GET_FILTERED_DATASET_CYCLE_DATA,
    )

  def get_filtered_metadata(
    self,
    filters: list[ByteratFilter],
    continuation_token: str | None = None,
  ) -> ByteratData:
    return self.__get_filtered_data(
      filters=filters,
      continuation_token=continuation_token,
      query_info=GET_FILTERED_METADATA,
    )
