
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class MicroWebSrvRoute:
    def __init__(self, route: Any, method: Any, func: Any, routeArgNames: Any, routeRegex: Any) -> None: ...
class MicroWebSrv:
    def route(cls: Any, url: Any, method: Any=) -> Any:
        #   0: return func
        # ? 0: return func
        #   1: return route_decorator
        # ? 1: return route_decorator
        def route_decorator(func: Any) -> Any: ...
            #   0: return func
            # ? 0: return func
    def HTMLEscape(s: str) -> Any: ...
        #   0: return .join(<gen MicroWebSrv._html_escape_chars.get(c,c) for c in s>)
        # ? 0: return .join(<gen MicroWebSrv._html_escape_chars.get(c, c) for c in str>)
    def _tryAllocByteArray(size: Any) -> Optional[Any]: ...
        #   0: return bytearray(size)
        # ? 0: return bytearray(size)
        #   1: return
        #   1: return
    def _tryStartThread(func: Any, args: Any=(), stacksize: Any=) -> Optional[Any]: ...
        #   0: return th
        # ? 0: return th
        #   1: return
        #   1: return
    def _unquote(s: str) -> Any: ...
        #   0: return .join(r)
        # ? 0: return .join(r)
    def _unquote_plus(s: str) -> Any: ...
        #   0: return MicroWebSrv._unquote(s.replace())
        # ? 0: return MicroWebSrv._unquote(str.replace())
    def _fileExists(path: Any) -> None: ...
    def _isPyHTMLFile(filename: str) -> Any: ...
        #   0: return filename.lower().endswith(MicroWebSrv._pyhtmlPagesExt)
        # ? 0: return str.lower().endswith(MicroWebSrv._pyhtmlPagesExt)
    def __init__(self, routeHandlers: Any=[], port: Any=, bindIP: Any=, webPath: Any=) -> None: ...
    def _serverProcess(self) -> None: ...
    def Start(self, threaded: Any=, stackSize: Any=) -> None: ...
    def Stop(self) -> None: ...
    def IsStarted(self) -> Any: ...
        #   0: return self._started
        # ? 0: return self._started
    def threadID(self) -> Any: ...
        #   0: return self.thID
        # ? 0: return self.thID
    def State(self) -> Any: ...
        #   0: return self._state
        # ? 0: return self._state
    def SetNotFoundPageUrl(self, url: Any=) -> None: ...
    def GetMimeTypeFromFilename(self, filename: str) -> Optional[Any]: ...
        #   0: return self._mimeTypes[ext]
        # ? 0: return self._mimeTypes[ext]
        #   1: return
        #   1: return
    def GetRouteHandler(self, resUrl: Any, method: Any) -> Union[Tuple[, ], Tuple[Any, Any], Tuple[Any, ]]: ...
    def _physPathFromURLPath(self, urlPath: Any) -> Optional[Any]: ...
        #   0: return physPath
        # ? 0: return physPath
        #   1: return physPath
        # ? 1: return physPath
        #   2: return
        #   2: return
        def __init__(self, microWebSrv: Any, socket: Any, addr: Any) -> None: ...
        def _processRequest(self) -> None: ...
        def _parseFirstLine(self, response: Any) -> None: ...
        def _parseHeader(self, response: Any) -> None: ...
        def _getConnUpgrade(self) -> Optional[Any]: ...
            #   0: return self._headers.get().lower()
            # ? 0: return self._headers.get().lower()
            #   1: return
            #   1: return
        def GetServer(self) -> Any: ...
            #   0: return self._microWebSrv
            # ? 0: return self._microWebSrv
        def GetAddr(self) -> Any: ...
            #   0: return self._addr
            # ? 0: return self._addr
        def GetIPAddr(self) -> Any: ...
            #   0: return self._addr[]
            # ? 0: return self._addr[]
        def GetPort(self) -> Any: ...
            #   0: return self._addr[]
            # ? 0: return self._addr[]
        def GetRequestMethod(self) -> Any: ...
            #   0: return self._method
            # ? 0: return self._method
        def GetRequestTotalPath(self) -> Any: ...
            #   0: return self._path
            # ? 0: return self._path
        def GetRequestPath(self) -> Any: ...
            #   0: return self._resPath
            # ? 0: return self._resPath
        def GetRequestQueryString(self) -> Any: ...
            #   0: return self._queryString
            # ? 0: return self._queryString
        def GetRequestQueryParams(self) -> Any: ...
            #   0: return self._queryParams
            # ? 0: return self._queryParams
        def GetRequestHeaders(self) -> Any: ...
            #   0: return self._headers
            # ? 0: return self._headers
        def GetRequestContentType(self) -> Any: ...
            #   0: return self._contentType
            # ? 0: return self._contentType
        def GetRequestContentLength(self) -> Any: ...
            #   0: return self._contentLength
            # ? 0: return self._contentLength
        def ReadRequestContent(self, size: Any=) -> Optional[Any]: ...
        def ReadRequestPostedFormData(self) -> Any: ...
            #   0: return res
            # ? 0: return res
        def ReadRequestContentAsJSON(self) -> Optional[Any]: ...
            #   0: return loads(self.ReadRequestContent())
            # ? 0: return loads(self.ReadRequestContent())
            #   1: return
            #   1: return
        def __init__(self, client: Any) -> None: ...
        def _write(self, data: Any) -> Any: ...
            #   0: return self._client._socket.write(data)
            # ? 0: return self._client._socket.write(data)
        def _writeFirstLine(self, code: Any) -> None: ...
        def _writeHeader(self, name: str, value: Any) -> None: ...
        def _writeContentTypeHeader(self, contentType: Any, charset: Any=) -> None: ...
        def _writeServerHeader(self) -> None: ...
        def _writeEndHeader(self) -> None: ...
        def _writeBeforeContent(self, code: Any, headers: Any, contentType: Any, contentCharset: Any, contentLength: Any) -> None: ...
        def WriteSwitchProto(self, upgrade: Any, headers: Any=) -> None: ...
        def WriteResponse(self, code: Any, headers: Any, contentType: Any, contentCharset: Any, content: Any) -> None: ...
        def WriteResponsePyHTMLFile(self, filepath: Any, headers: Any=) -> Any: ...
            #   0: return self.WriteResponse(headers,tmplResult)
            # ? 0: return self.WriteResponse(headers, tmplResult)
            #   1: return self.WriteResponse(self._execErrCtnTmpl%{:, :str(ex)})
            # ? 1: return self.WriteResponse(self._execErrCtnTmpl%Dict[{:, :str(ex)}])
            #   2: return self.WriteResponseNotImplemented()
            # ? 2: return self.WriteResponseNotImplemented()
        def WriteResponseFile(self, filepath: Any, contentType: Any=, headers: Any=) -> None: ...
        def WriteResponseFileAttachment(self, filepath: Any, attachmentName: Any, headers: Any=) -> Any: ...
            #   0: return self.WriteResponseFile(filepath,headers)
            # ? 0: return self.WriteResponseFile(filepath, headers)
        def WriteResponseOk(self, headers: Any=, contentType: Any=, contentCharset: Any=, content: Any=) -> Any: ...
            #   0: return self.WriteResponse(headers,contentType,contentCharset,content)
            # ? 0: return self.WriteResponse(headers, contentType, contentCharset, content)
        def WriteResponseJSONOk(self, obj: Any=, headers: Any=) -> Any: ...
            #   0: return self.WriteResponse(headers,dumps(obj))
            # ? 0: return self.WriteResponse(headers, dumps(obj))
        def WriteResponseRedirect(self, location: Any) -> Any: ...
            #   0: return self.WriteResponse(headers)
            # ? 0: return self.WriteResponse(headers)
        def WriteResponseError(self, code: Any) -> Any: ...
            #   0: return self.WriteResponse(code,self._errCtnTmpl%{:code, :responseCode[], :responseCode[]})
            # ? 0: return self.WriteResponse(code, self._errCtnTmpl%Dict[{:code, :responseCode[], :responseCode[]}])
        def WriteResponseJSONError(self, code: Any, obj: Any=) -> Any: ...
            #   0: return self.WriteResponse(code,dumps(obj if obj else {} ))
            # ? 0: return self.WriteResponse(code, dumps(Union[Any, Dict[{}]]))
        def WriteResponseBadRequest(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()
        def WriteResponseForbidden(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()
        def WriteResponseNotFound(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()
        def WriteResponseMethodNotAllowed(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()
        def WriteResponseInternalServerError(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()
        def WriteResponseNotImplemented(self) -> Any: ...
            #   0: return self.WriteResponseError()
            # ? 0: return self.WriteResponseError()