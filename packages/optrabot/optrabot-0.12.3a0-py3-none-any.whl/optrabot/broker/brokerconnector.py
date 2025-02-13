from abc import ABC, abstractmethod
from typing import List
from eventkit import Event
from loguru import logger

from optrabot.broker.order import Order as GenericOrder, OrderStatus
from optrabot.config import Config
from optrabot.models import Account
from optrabot.tradetemplate.templatefactory import Template

class BrokerConnector(ABC):
	def __init__(self) -> None:
		self._initialized = False
		self._createEvents()
		self.id = None		# ID of the connector
		self.broker = None	# ID of the broker
		self._tradingEnabled = False
		self._managedAccounts: List[Account] = []
		pass
	
	@abstractmethod
	async def cancel_order(self, order: GenericOrder):
		"""
		Cancels the given order
		"""
		pass

	@abstractmethod
	async def connect(self):
		""" 
		Establishes a connection to the broker
		"""
		logger.info('Connecting with broker {}', self.id)

	@abstractmethod
	async def disconnect(self):
		""" 
		Disconnects from the broker
		"""
		logger.info('Disconnecting from broker {}', self.id)

	@abstractmethod
	def isConnected(self) -> bool:
		""" 
		Returns True if the broker is connected
		"""
		pass

	@abstractmethod
	def getAccounts(self) -> List[Account]:
		""" 
		Returns the accounts managed by the broker connection
		"""
		pass
	
	@abstractmethod
	async def prepareOrder(self, order: GenericOrder) -> bool:
		"""
		Prepares the given order for execution.
		- Retrieve current market data for order legs

		It returns True, if the order could be prepared successfully
		"""

	@abstractmethod
	async def placeOrder(self, order: GenericOrder, template: Template):
		""" 
		Places the given order for a managed account via the broker connection
		"""
		pass

	@abstractmethod
	async def adjustOrder(self, order: GenericOrder, price: float) -> bool:
		""" 
		Adjusts the given order with the given new price
		"""
		pass

	@abstractmethod
	async def requestTickerData(self, symbols: List[str]):
		""" 
		Request ticker data for the given symbols and their options
		"""
		pass

	@abstractmethod
	def getFillPrice(self, order: GenericOrder) -> float:
		""" 
		Returns the fill price of the given order if it is filled
		"""
		pass

	def getLastPrice(self, symbol: str) -> float:
		""" 
		Returns the last price of the given symbol
		"""
		pass

	@abstractmethod
	def get_strike_by_delta(self, symbol: str, right: str, delta: int) -> float:
		""" 
		Returns the strike price based on the given delta based on the buffered option price data
		"""
		raise NotImplementedError()
	
	async def eod_settlement_tasks(self):
		"""
		Perform End of Day settlement tasks
		"""
		pass

	def _createEvents(self):
		""" 
		Creates the events for the broker connection
		"""
		self.connectedEvent = Event('connectedEvent')
		self.disconnectedEvent = Event('disconnectEvent')
		self.connectFailedEvent = Event('connectFailedEvent')
		self.orderStatusEvent = Event('orderStatusEvent')

	def _emitConnectedEvent(self):
		""" 
		Emits the connected event
		"""
		self.connectedEvent.emit(self)

	def _emitDisconnectedEvent(self):
		""" 
		Emits the disconnected event
		"""
		self._managedAccounts = []
		self.disconnectedEvent.emit(self)

	def _emitConnectFailedEvent(self):
		""" 
		Emits the broker connect failed event
		"""
		self.connectFailedEvent.emit(self)

	def _emitOrderStatusEvent(self, order: GenericOrder, status: OrderStatus, filledAmount: int = 0):
		""" 
		Emits the order status event. Filled amount holds the amount that has been filled with this
		order status change, if the status event is a "Filled" event.
		"""
		self.orderStatusEvent.emit(order, status, filledAmount)

	def isInitialized(self) -> bool:
		""" 
		Returns True if the broker connector is initialized
		"""
		return self._initialized

	def isTradingEnabled(self) -> bool:
		""" 
		Returns True if trading is enabled
		"""
		return self._tradingEnabled