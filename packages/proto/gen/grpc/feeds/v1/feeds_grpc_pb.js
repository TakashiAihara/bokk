// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var feeds_v1_feeds_pb = require('../../feeds/v1/feeds_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');

function serialize_feeds_v1_CreateFeedRequest(arg) {
  if (!(arg instanceof feeds_v1_feeds_pb.CreateFeedRequest)) {
    throw new Error('Expected argument of type feeds.v1.CreateFeedRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_feeds_v1_CreateFeedRequest(buffer_arg) {
  return feeds_v1_feeds_pb.CreateFeedRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_feeds_v1_Feed(arg) {
  if (!(arg instanceof feeds_v1_feeds_pb.Feed)) {
    throw new Error('Expected argument of type feeds.v1.Feed');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_feeds_v1_Feed(buffer_arg) {
  return feeds_v1_feeds_pb.Feed.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_feeds_v1_GetFeedRequest(arg) {
  if (!(arg instanceof feeds_v1_feeds_pb.GetFeedRequest)) {
    throw new Error('Expected argument of type feeds.v1.GetFeedRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_feeds_v1_GetFeedRequest(buffer_arg) {
  return feeds_v1_feeds_pb.GetFeedRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_feeds_v1_ListFeedsRequest(arg) {
  if (!(arg instanceof feeds_v1_feeds_pb.ListFeedsRequest)) {
    throw new Error('Expected argument of type feeds.v1.ListFeedsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_feeds_v1_ListFeedsRequest(buffer_arg) {
  return feeds_v1_feeds_pb.ListFeedsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_feeds_v1_ListFeedsResponse(arg) {
  if (!(arg instanceof feeds_v1_feeds_pb.ListFeedsResponse)) {
    throw new Error('Expected argument of type feeds.v1.ListFeedsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_feeds_v1_ListFeedsResponse(buffer_arg) {
  return feeds_v1_feeds_pb.ListFeedsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var FeedServiceService = exports.FeedServiceService = {
  getFeed: {
    path: '/feeds.v1.FeedService/GetFeed',
    requestStream: false,
    responseStream: false,
    requestType: feeds_v1_feeds_pb.GetFeedRequest,
    responseType: feeds_v1_feeds_pb.Feed,
    requestSerialize: serialize_feeds_v1_GetFeedRequest,
    requestDeserialize: deserialize_feeds_v1_GetFeedRequest,
    responseSerialize: serialize_feeds_v1_Feed,
    responseDeserialize: deserialize_feeds_v1_Feed,
  },
  listFeeds: {
    path: '/feeds.v1.FeedService/ListFeeds',
    requestStream: false,
    responseStream: false,
    requestType: feeds_v1_feeds_pb.ListFeedsRequest,
    responseType: feeds_v1_feeds_pb.ListFeedsResponse,
    requestSerialize: serialize_feeds_v1_ListFeedsRequest,
    requestDeserialize: deserialize_feeds_v1_ListFeedsRequest,
    responseSerialize: serialize_feeds_v1_ListFeedsResponse,
    responseDeserialize: deserialize_feeds_v1_ListFeedsResponse,
  },
  createFeed: {
    path: '/feeds.v1.FeedService/CreateFeed',
    requestStream: false,
    responseStream: false,
    requestType: feeds_v1_feeds_pb.CreateFeedRequest,
    responseType: feeds_v1_feeds_pb.Feed,
    requestSerialize: serialize_feeds_v1_CreateFeedRequest,
    requestDeserialize: deserialize_feeds_v1_CreateFeedRequest,
    responseSerialize: serialize_feeds_v1_Feed,
    responseDeserialize: deserialize_feeds_v1_Feed,
  },
};

exports.FeedServiceClient = grpc.makeGenericClientConstructor(FeedServiceService);
