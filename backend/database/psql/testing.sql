CREATE TABLE IF NOT EXISTS users (
  username VARCHAR(16) PRIMARY KEY,
  first_name VARCHAR(16),
  email VARCHAR(32),
  birthday date,
  membership date,
  session_num int,
  isOrthodox bool,
  picture VARCHAR(65635)
);

CREATE TABLE IF NOT EXISTS sessions (
  session_id INT PRIMARY KEY,
  username VARCHAR(50),
  category VARCHAR(12),
  datetime TIMESTAMP,
  duration INTERVAL,
  metrics JSON,
  CONSTRAINT FK_username FOREIGN KEY(username)
  	REFERENCES users(username)
  
);

CREATE TABLE metrics (
  username VARCHAR(50) PRIMARY KEY,
  forces real,
  accuracy real,
  reaction real,
  form real,
  stability real

);

CREATE TABLE IF NOT EXISTS probs (
  username VARCHAR(16) PRIMARY KEY,
  q1 REAL,
  q2 REAL,
  q3 REAL,
  q4 REAL,
  hook REAL,
  uppercut REAL,
  straight REAL,
  CONSTRAINT FK_username FOREIGN KEY(username)
  	REFERENCES users(username)

);

INSERT INTO probs
VALUES ('test', 0.5, 0.5, 0.5, 0.5, 0.33, 0.33, 0.33);

INSERT INTO users
VALUES ('GingaNinja', 'Brandon', 'brandon@email.com',
'1999-03-28', '2022-09-08', 88, True, 'base64: "data:image/png;base64, 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"');

INSERT INTO metrics
VALUES ('GingaNinja', 530, 87, 325, 65, 80);

INSERT INTO sessions(session_id, username, category, datetime, duration, metrics)
VALUES (2, 'GingaNinja', 'Personalized', '2023-01-01 00:00:00', '0 0:01:15', 
       '{"metrics": {
                "hook": {
                    "force": {
                        "avg": 341.57,
                        "quads": [
                            350.0,
                            337.0,
                            350.0,
                            337.0
                        ]
                    },
                    "reaction": {
                        "avg": 375.18,
                        "quads": [
                            325.0,
                            400.0,
                            325.0,
                            400.0
                        ]
                    },
                    "accuracy": {
                        "avg": 100.0,
                        "quads": [
                            100.0,
                            100.0,
                            100.0,
                            100.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "uppercut": {
                    "force": {
                        "avg": 238.35,
                        "quads": [
                            0.0,
                            318.0,
                            318.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 984.52,
                        "quads": [
                            3000.0,
                            313.0,
                            313.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 75.0,
                        "quads": [
                            0.0,
                            100.0,
                            100.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "straight": {
                    "force": {
                        "avg": 66.67,
                        "quads": [
                            0.0,
                            0.0,
                            100.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 2116.67,
                        "quads": [
                            3000.0,
                            0.0,
                            1675.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 33.33,
                        "quads": [
                            0.0,
                            0.0,
                            50.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "performance": {
                    "avg": 64.64,
                    "data": [
                        65.22,
                        30.21,
                        99.45,
                        100.0,
                        49.86,
                        65.22,
                        30.21,
                        99.45,
                        100.0,
                        49.86,
                        65.22,
                        30.21,
                        99.45,
                        100.0,
                        0.0,
                        49.86
                    ]
                }
            }}');
 
 INSERT INTO users 
VALUES ('test', 'Bobert', 'test@test.com', '2023-01-01', '2023-02-02', 0,  True, 'data:image/png;base64, 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');

INSERT INTO metrics
VALUES ('test', 200, 99.99, 160, 80, 45);

INSERT INTO sessions
VALUES (69, 'test', 'Speed', '2023-03-19 20:16:04', '0 0:00:30', '{"metrics": {
                "hook": {
                    "force": {
                        "avg": 341.57,
                        "quads": [
                            350.0,
                            337.0,
                            350.0,
                            337.0
                        ]
                    },
                    "reaction": {
                        "avg": 375.18,
                        "quads": [
                            325.0,
                            400.0,
                            325.0,
                            400.0
                        ]
                    },
                    "accuracy": {
                        "avg": 100.0,
                        "quads": [
                            100.0,
                            100.0,
                            100.0,
                            100.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "uppercut": {
                    "force": {
                        "avg": 238.35,
                        "quads": [
                            0.0,
                            318.0,
                            318.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 984.52,
                        "quads": [
                            3000.0,
                            313.0,
                            313.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 75.0,
                        "quads": [
                            0.0,
                            100.0,
                            100.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "straight": {
                    "force": {
                        "avg": 66.67,
                        "quads": [
                            0.0,
                            0.0,
                            100.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 2116.67,
                        "quads": [
                            3000.0,
                            0.0,
                            1675.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 33.33,
                        "quads": [
                            0.0,
                            0.0,
                            50.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "performance": {
                    "avg": 39.44,
                    "data": [
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        25.0,
                        36.0
                    ]
                }
            }}');
    
INSERT INTO users
VALUES ('SlimShady', 'Labib', 'labib@email.com',
'1999-11-22', '2022-09-08', 69, False, 'base64: "data:image/png;base64, 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"');

INSERT INTO metrics
VALUES ('SlimShady', 999, 90, 400, 75, 77);

INSERT INTO sessions
VALUES (01, 'SlimShady', 'Speed', '2023-03-25 20:16:04', '0 3:10:30', '{"metrics": {
                "hook": {
                    "force": {
                        "avg": 341.57,
                        "quads": [
                            350.0,
                            337.0,
                            350.0,
                            337.0
                        ]
                    },
                    "reaction": {
                        "avg": 375.18,
                        "quads": [
                            325.0,
                            400.0,
                            325.0,
                            400.0
                        ]
                    },
                    "accuracy": {
                        "avg": 100.0,
                        "quads": [
                            100.0,
                            100.0,
                            100.0,
                            100.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "uppercut": {
                    "force": {
                        "avg": 238.35,
                        "quads": [
                            0.0,
                            318.0,
                            318.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 984.52,
                        "quads": [
                            3000.0,
                            313.0,
                            313.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 75.0,
                        "quads": [
                            0.0,
                            100.0,
                            100.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "straight": {
                    "force": {
                        "avg": 66.67,
                        "quads": [
                            0.0,
                            0.0,
                            100.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 2116.67,
                        "quads": [
                            3000.0,
                            0.0,
                            1675.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 33.33,
                        "quads": [
                            0.0,
                            0.0,
                            50.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "performance": {
                    "avg": 39.44,
                    "data": [
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        25.0,
                        36.0
                    ]
                }
            }}');
            
INSERT INTO sessions
VALUES (04, 'SlimShady', 'Speed', '2023-03-25 20:16:04', '0 3:10:30', '{"metrics": {
                "hook": {
                    "force": {
                        "avg": 341.57,
                        "quads": [
                            350.0,
                            337.0,
                            350.0,
                            337.0
                        ]
                    },
                    "reaction": {
                        "avg": 375.18,
                        "quads": [
                            325.0,
                            400.0,
                            325.0,
                            400.0
                        ]
                    },
                    "accuracy": {
                        "avg": 100.0,
                        "quads": [
                            100.0,
                            100.0,
                            100.0,
                            100.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "uppercut": {
                    "force": {
                        "avg": 238.35,
                        "quads": [
                            0.0,
                            318.0,
                            318.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 984.52,
                        "quads": [
                            3000.0,
                            313.0,
                            313.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 75.0,
                        "quads": [
                            0.0,
                            100.0,
                            100.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "straight": {
                    "force": {
                        "avg": 66.67,
                        "quads": [
                            0.0,
                            0.0,
                            100.0,
                            0.0
                        ]
                    },
                    "reaction": {
                        "avg": 2116.67,
                        "quads": [
                            3000.0,
                            0.0,
                            1675.0,
                            0.0
                        ]
                    },
                    "accuracy": {
                        "avg": 33.33,
                        "quads": [
                            0.0,
                            0.0,
                            50.0,
                            0.0
                        ]
                    },
                    "form": {
                        "avg": 0.0,
                        "quads": [
                            0.0,
                            0.0,
                            0.0,
                            0.0
                        ]
                    }
                },
                "performance": {
                    "avg": 39.44,
                    "data": [
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        36.0,
                        40.0,
                        32.0,
                        47.0,
                        47.0,
                        25.0,
                        36.0
                    ]
                }
            }}');