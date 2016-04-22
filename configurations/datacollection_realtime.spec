[{
  "dataSchema": {
    "dataSource": "datacollector",
    "parser": {
      "type": "json",
      "parseSpec": {
        "format": "json",
        "timestampSpec": {
          "column": "timestamp",
          "format": "auto"
        },
        "dimensionsSpec": {
          "dimensions": [
            "key",
            "value",
	    "node"
          ],
          "dimensionExclusions": [],
          "spatialDimensions": []
        }
      }
    },
    "metricsSpec": [
      {
        "type": "count",
        "name": "messages"
      },
      { 
	"type" : "doubleMin", 
	"name" : "minimum", 
	"fieldName" : "value" 
      },
      { 
	"type" : "doubleMax", 
	"name" : "maximum", 
	"fieldName" : "value" 
      },
      { 
	"type": "javascript",
	"name": "average",
	  "fieldNames"  : [ "value" ],
	  "fnAggregate" : "function(current, value) { return current + value; }",
	  "fnCombine"   : "function(partialA, partialB) { return partialA + partialB; }",
	  "fnReset"     : "function() { return 0; }"
	}
    ],
    "granularitySpec": {
      "type": "uniform",
      "segmentGranularity": "HOUR",
      "queryGranularity": "NONE"
    }
  },
  "ioConfig": {
    "type": "realtime",
    "firehose": {
      "type": "rabbitmq",
      "connection" : {
        "host": "localhost",
        "port": "5672",
        "username": "druid",
        "password": "diurd",
        "virtualHost": "druid"
      },
      "config" : {
        "exchange": "data-exchange",
        "queue" : "data",
        "routingKey": "#",
        "durable": "true",
        "exclusive": "false",
        "autoDelete": "false",
        "maxRetries": "10",
        "retryIntervalSeconds": "1",
        "maxDurationSeconds": "300"
      }
    },
    "plumber": {
      "type": "realtime"
    }
  },
  "tuningConfig": {
    "type": "realtime",
    "maxRowsInMemory": 500000,
    "intermediatePersistPeriod": "PT10m",
    "windowPeriod": "PT10m",
    "basePersistDirectory": "\/tmp\/realtime\/basePersist",
    "rejectionPolicy": {
      "type": "serverTime"
    }
  }
}]

