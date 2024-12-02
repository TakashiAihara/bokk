// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var bookmarks_v1_bookmarks_pb = require('../../bookmarks/v1/bookmarks_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');

function serialize_bookmarks_v1_Bookmark(arg) {
  if (!(arg instanceof bookmarks_v1_bookmarks_pb.Bookmark)) {
    throw new Error('Expected argument of type bookmarks.v1.Bookmark');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_bookmarks_v1_Bookmark(buffer_arg) {
  return bookmarks_v1_bookmarks_pb.Bookmark.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_bookmarks_v1_CreateBookmarkRequest(arg) {
  if (!(arg instanceof bookmarks_v1_bookmarks_pb.CreateBookmarkRequest)) {
    throw new Error('Expected argument of type bookmarks.v1.CreateBookmarkRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_bookmarks_v1_CreateBookmarkRequest(buffer_arg) {
  return bookmarks_v1_bookmarks_pb.CreateBookmarkRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_bookmarks_v1_GetBookmarkRequest(arg) {
  if (!(arg instanceof bookmarks_v1_bookmarks_pb.GetBookmarkRequest)) {
    throw new Error('Expected argument of type bookmarks.v1.GetBookmarkRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_bookmarks_v1_GetBookmarkRequest(buffer_arg) {
  return bookmarks_v1_bookmarks_pb.GetBookmarkRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_bookmarks_v1_ListBookmarksRequest(arg) {
  if (!(arg instanceof bookmarks_v1_bookmarks_pb.ListBookmarksRequest)) {
    throw new Error('Expected argument of type bookmarks.v1.ListBookmarksRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_bookmarks_v1_ListBookmarksRequest(buffer_arg) {
  return bookmarks_v1_bookmarks_pb.ListBookmarksRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_bookmarks_v1_ListBookmarksResponse(arg) {
  if (!(arg instanceof bookmarks_v1_bookmarks_pb.ListBookmarksResponse)) {
    throw new Error('Expected argument of type bookmarks.v1.ListBookmarksResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_bookmarks_v1_ListBookmarksResponse(buffer_arg) {
  return bookmarks_v1_bookmarks_pb.ListBookmarksResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var BookmarkServiceService = exports.BookmarkServiceService = {
  getBookmark: {
    path: '/bookmarks.v1.BookmarkService/GetBookmark',
    requestStream: false,
    responseStream: false,
    requestType: bookmarks_v1_bookmarks_pb.GetBookmarkRequest,
    responseType: bookmarks_v1_bookmarks_pb.Bookmark,
    requestSerialize: serialize_bookmarks_v1_GetBookmarkRequest,
    requestDeserialize: deserialize_bookmarks_v1_GetBookmarkRequest,
    responseSerialize: serialize_bookmarks_v1_Bookmark,
    responseDeserialize: deserialize_bookmarks_v1_Bookmark,
  },
  listBookmarks: {
    path: '/bookmarks.v1.BookmarkService/ListBookmarks',
    requestStream: false,
    responseStream: false,
    requestType: bookmarks_v1_bookmarks_pb.ListBookmarksRequest,
    responseType: bookmarks_v1_bookmarks_pb.ListBookmarksResponse,
    requestSerialize: serialize_bookmarks_v1_ListBookmarksRequest,
    requestDeserialize: deserialize_bookmarks_v1_ListBookmarksRequest,
    responseSerialize: serialize_bookmarks_v1_ListBookmarksResponse,
    responseDeserialize: deserialize_bookmarks_v1_ListBookmarksResponse,
  },
  createBookmark: {
    path: '/bookmarks.v1.BookmarkService/CreateBookmark',
    requestStream: false,
    responseStream: false,
    requestType: bookmarks_v1_bookmarks_pb.CreateBookmarkRequest,
    responseType: bookmarks_v1_bookmarks_pb.Bookmark,
    requestSerialize: serialize_bookmarks_v1_CreateBookmarkRequest,
    requestDeserialize: deserialize_bookmarks_v1_CreateBookmarkRequest,
    responseSerialize: serialize_bookmarks_v1_Bookmark,
    responseDeserialize: deserialize_bookmarks_v1_Bookmark,
  },
};

exports.BookmarkServiceClient = grpc.makeGenericClientConstructor(BookmarkServiceService);
