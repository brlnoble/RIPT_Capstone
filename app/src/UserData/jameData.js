const userData = {

    //Basic profile information
    profile: {
        userName: "JT_Experience",
        firstName: "Jame",
        email: "jame@email.com",
        birthday: "August 2, 1999",
        member: "September 8, 2022",
        sessions: "420", //this might not be needed
        stance: "Orthodox",
        picture: { //encode user profile picture as base64 string
            base64: "data:image/png;base64, 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"
        },
    },

    //Average values for all the metrics, displayed on profile
    averageMetrics: {
        force: "999 N",
        accuracy: "90%",
        reaction: "400 ms",
        form: "75%",
        stability: "77%",
    },

    //The session object
    sessions: [
        //First session
        {
            key: "12345", //Unique for each session
            sessionInfo: { //General information about the session
                category: "Personalized",
                date: "Feb. 23, 2023",
                time: "3:09 PM",
                duration: "3m 30s",
            },
            punchData: [ //Contains all the data regading the punches
                {
                    type: "Uppercut", 
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Cross",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Straight",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },
            ] 
        },

        //Second session
        {
            key: "54321", //Unique for each session
            sessionInfo: { //General information about the session
                category: "Endurance",
                date: "Feb. 24, 2023",
                time: "10:27 AM",
                duration: "5m 00s",
            },
            punchData: [ //Contains all the data regading the punches
                {
                    type: "Uppercut", 
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Cross",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Straight",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },
            ]
        },

        //Second session
        {
            key: "98765", //Unique for each session
            sessionInfo: { //General information about the session
                category: "Personalized",
                date: "Feb. 24, 2023",
                time: "10:32 AM",
                duration: "3m 00s",
            },
            punchData: [ //Contains all the data regading the punches
                {
                    type: "Uppercut", 
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Cross",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },

                {
                    type: "Straight",
                    metrics: {
                        force: {
                            avg: "250 N", 
                            quads: {
                                q1: 100, 
                                q2: 200, 
                                q3: 300, 
                                q4: 400
                            }
                        }, 
                        accuracy: {
                            avg: "92%", 
                            quads: {
                                q1: 90, 
                                q2: 90, 
                                q3: 88, 
                                q4: 100
                            }
                        }, 
                        reaction: {
                            avg: "315 ms", 
                            quads: {
                                q1: 335, 
                                q2: 295, 
                                q3: 310, 
                                q4: 320
                            }
                        }, 
                        form: {
                            avg: "60%", 
                            quads: {
                                q1: 65, 
                                q2: 62, 
                                q3: 50, 
                                q4: 63
                            }
                        }, 
                        stability: {
                            avg: 70,
                            chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72] //Array of information per punch
                        }
                    }
                },
            ]
        },
    ]
}

export default userData