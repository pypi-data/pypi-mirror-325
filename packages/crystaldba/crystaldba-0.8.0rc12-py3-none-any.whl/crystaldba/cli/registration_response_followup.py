# from ..shared.api import ChatMessage, ChatRequest, ChatResponse, StartupMessage
# from .chat_response_followup import ChatResponseFollowupProtocol


# class RegistrationResponseFollowup(ChatResponseFollowupProtocol):
#     """Protocol defining the interface for chat stepping functionality."""

#     message_counter: int = 0
#     continuation_token: str | None = None


#     def create_chatrequest(self, message: ChatMessage | StartupMessage) -> ChatRequest:
#         match message:
#             case StartupMessage():
#                 return ChatRequest(
#                     sequence_id=0,
#                     continuation_token=None,
#                     payload=message,
#                 )
#             case ChatMessage():
#                 self.message_counter += 1
#                 return ChatRequest(
#                     sequence_id=self.message_counter,
#                     continuation_token=self.continuation_token,
#                     payload=message,
#                 )


#     def from_chatresponse_to_possible_new_chatrequest(self, chat_response: ChatResponse) -> str | ChatRequest | None:
#         chat_response.payload match:
#             case ChatMessage:

#                 return None
#             case ChatMessage():
#                 return chat_response.payload.message
