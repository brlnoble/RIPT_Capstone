const userData = {

    //Basic profile information
    profile: {
        userName: "SlimShady",
        firstName: "Labib",
        email: "labib@email.com",
        birthday: "November 22, 1999",
        member: "September 8, 2022",
        sessions: "69", //this might not be needed
        stance: "Southpaw",
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

        //Third session
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

        //Fourth session
        {
            key: "56789", //Unique for each session
            sessionInfo: { //General information about the session
                category: "Speed",
                date: "Feb. 24, 2023",
                time: "4:31 PM",
                duration: "2m 00s",
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