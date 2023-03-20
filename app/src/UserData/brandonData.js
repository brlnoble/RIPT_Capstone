const userData = {

    //Basic profile information
    profile: {
        userName: "GingaNinja",
        firstName: "Brandon",
        email: "brandon@email.com",
        birthday: "March 28, 1999",
        member: "September 8, 2022",
        sessions: "88", //this might not be needed
        stance: "Orthodox",
        picture: { //encode user profile picture as base64 string
            base64: "data:image/png;base64, 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"
        },
    },

    //Average values for all the metrics, displayed on profile
    averageMetrics: {
        force: "530 N",
        accuracy: "87%",
        reaction: "325 ms",
        form: "65%",
        performance: "80%",
    },

    //The session object
    sessions: [
        //First session
        {
            "id": "",
            "username": "",
            "category": "Personalized",
            "datetime": "2023-03-19 20:16:04",
            "duration": "0 0:00:30",
            "metrics": {
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
            }
        },

        //Second session
        {
            "id": "",
            "username": "",
            "category": "Personalized",
            "datetime": "2023-03-19 19:40:08",
            "duration": "0 0:00:30",
            "metrics": {
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
            }
        },
    ]
}

export default userData