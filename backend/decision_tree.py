class Node:
    def __init__(self, question=None, yes=None, no=None, recommendation=None, instructions=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.recommendation = recommendation
        self.instructions = instructions

def build_tree():
    tree = Node(
        question="Is the pain in the lower back?",
        yes=Node(
            question="Is the pain radiating down the leg?",
            yes=Node(
                question="Is the pain sharp?",
                yes=Node(
                    recommendation="Sciatica sharp pain exercises",
                    instructions="To perform Sciatica sharp pain exercises:\n1. Lie on your back with both legs bent.\n2. Slowly bring one knee to your chest.\n3. Hold for 30 seconds, then switch legs.\n4. Repeat 3 times on each side."
                ),
                no=Node(
                    recommendation="Sciatica dull pain exercises",
                    instructions="To perform Sciatica dull pain exercises:\n1. Sit on the floor with your legs extended.\n2. Lean forward and reach for your toes.\n3. Hold for 30 seconds.\n4. Repeat 3 times."
                )
            ),
            no=Node(
                question="Is the pain constant?",
                yes=Node(
                    recommendation="Lower back constant pain exercises",
                    instructions="To perform Lower back constant pain exercises:\n1. Lie on your stomach.\n2. Lift your chest off the ground while keeping your hips down.\n3. Hold for 10 seconds.\n4. Repeat 10 times."
                ),
                no=Node(
                    recommendation="Lower back occasional pain exercises",
                    instructions="To perform Lower back occasional pain exercises:\n1. Stand with your feet shoulder-width apart.\n2. Bend forward and touch your toes.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                )
            )
        ),
        no=Node(
            question="Is the pain in the shoulder?",
            yes=Node(
                question="Is the pain in the right shoulder?",
                yes=Node(
                    question="Is the pain in the front part of the shoulder?",
                    yes=Node(
                        recommendation="Right front shoulder exercises",
                        instructions="To perform Right front shoulder exercises:\n1. Stand with your back against a wall.\n2. Raise your right arm to shoulder height.\n3. Press your hand against the wall.\n4. Hold for 20 seconds.\n5. Repeat 5 times."
                    ),
                    no=Node(
                        recommendation="Right back shoulder exercises",
                        instructions="To perform Right back shoulder exercises:\n1. Stand with your left side against a wall.\n2. Raise your right arm and press the back of your hand against the wall.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                    )
                ),
                no=Node(
                    question="Is the pain in the front part of the shoulder?",
                    yes=Node(
                        recommendation="Left front shoulder exercises",
                        instructions="To perform Left front shoulder exercises:\n1. Stand with your back against a wall.\n2. Raise your left arm to shoulder height.\n3. Press your hand against the wall.\n4. Hold for 20 seconds.\n5. Repeat 5 times."
                    ),
                    no=Node(
                        recommendation="Left back shoulder exercises",
                        instructions="To perform Left back shoulder exercises:\n1. Stand with your right side against a wall.\n2. Raise your left arm and press the back of your hand against the wall.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                    )
                )
            ),
            no=Node(
                question="Is the pain in the knee?",
                yes=Node(
                    question="Is the pain in the right knee?",
                    yes=Node(
                        question="Is the pain on the inside of the knee?",
                        yes=Node(
                            recommendation="Right inside knee exercises",
                            instructions="To perform Right inside knee exercises:\n1. Sit on the floor with your legs extended.\n2. Place a small ball under your right knee.\n3. Press down gently.\n4. Hold for 10 seconds.\n5. Repeat 10 times."
                        ),
                        no=Node(
                            recommendation="Right outside knee exercises",
                            instructions="To perform Right outside knee exercises:\n1. Sit on the floor with your legs extended.\n2. Place a small ball under your right knee.\n3. Press down gently.\n4. Hold for 10 seconds.\n5. Repeat 10 times."
                        )
                    ),
                    no=Node(
                        question="Is the pain on the inside of the knee?",
                        yes=Node(
                            recommendation="Left inside knee exercises",
                            instructions="To perform Left inside knee exercises:\n1. Sit on the floor with your legs extended.\n2. Place a small ball under your left knee.\n3. Press down gently.\n4. Hold for 10 seconds.\n5. Repeat 10 times."
                        ),
                        no=Node(
                            recommendation="Left outside knee exercises",
                            instructions="To perform Left outside knee exercises:\n1. Sit on the floor with your legs extended.\n2. Place a small ball under your left knee.\n3. Press down gently.\n4. Hold for 10 seconds.\n5. Repeat 10 times."
                        )
                    )
                ),
                no=Node(
                    question="Is the pain in the ankle?",
                    yes=Node(
                        question="Is the pain in the right ankle?",
                        yes=Node(
                            question="Is the pain on the inside of the ankle?",
                            yes=Node(
                                recommendation="Right inside ankle exercises",
                                instructions="To perform Right inside ankle exercises:\n1. Sit on a chair with your right foot on the ground.\n2. Place a small ball under your right arch.\n3. Roll the ball back and forth gently.\n4. Repeat for 2 minutes."
                            ),
                            no=Node(
                                recommendation="Right outside ankle exercises",
                                instructions="To perform Right outside ankle exercises:\n1. Sit on a chair with your right foot on the ground.\n2. Place a small ball under your right arch.\n3. Roll the ball back and forth gently.\n4. Repeat for 2 minutes."
                            )
                        ),
                        no=Node(
                            question="Is the pain on the inside of the ankle?",
                            yes=Node(
                                recommendation="Left inside ankle exercises",
                                instructions="To perform Left inside ankle exercises:\n1. Sit on a chair with your left foot on the ground.\n2. Place a small ball under your left arch.\n3. Roll the ball back and forth gently.\n4. Repeat for 2 minutes."
                            ),
                            no=Node(
                                recommendation="Left outside ankle exercises",
                                instructions="To perform Left outside ankle exercises:\n1. Sit on a chair with your left foot on the ground.\n2. Place a small ball under your left arch.\n3. Roll the ball back and forth gently.\n4. Repeat for 2 minutes."
                            )
                        )
                    ),
                    no=Node(
                        question="Is the pain in the hip?",
                        yes=Node(
                            question="Is the pain in the right hip?",
                            yes=Node(
                                question="Is the pain in the front part of the hip?",
                                yes=Node(
                                    recommendation="Right front hip exercises",
                                    instructions="To perform Right front hip exercises:\n1. Lie on your back with your legs bent.\n2. Slowly bring your right knee to your chest.\n3. Hold for 30 seconds.\n4. Repeat 3 times."
                                ),
                                no=Node(
                                    recommendation="Right back hip exercises",
                                    instructions="To perform Right back hip exercises:\n1. Lie on your back with your legs bent.\n2. Slowly bring your right knee to your chest.\n3. Hold for 30 seconds.\n4. Repeat 3 times."
                                )
                            ),
                            no=Node(
                                question="Is the pain in the front part of the hip?",
                                yes=Node(
                                    recommendation="Left front hip exercises",
                                    instructions="To perform Left front hip exercises:\n1. Lie on your back with your legs bent.\n2. Slowly bring your left knee to your chest.\n3. Hold for 30 seconds.\n4. Repeat 3 times."
                                ),
                                no=Node(
                                    recommendation="Left back hip exercises",
                                    instructions="To perform Left back hip exercises:\n1. Lie on your back with your legs bent.\n2. Slowly bring your left knee to your chest.\n3. Hold for 30 seconds.\n4. Repeat 3 times."
                                )
                            )
                        ),
                        no=Node(
                            question="Is the pain in the wrist?",
                            yes=Node(
                                question="Is the pain in the right wrist?",
                                yes=Node(
                                    question="Is the pain on the top of the wrist?",
                                    yes=Node(
                                        recommendation="Right top wrist exercises",
                                        instructions="To perform Right top wrist exercises:\n1. Sit with your right arm extended and palm facing down.\n2. Use your left hand to gently pull back on your right fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                    ),
                                    no=Node(
                                        recommendation="Right bottom wrist exercises",
                                        instructions="To perform Right bottom wrist exercises:\n1. Sit with your right arm extended and palm facing up.\n2. Use your left hand to gently pull back on your right fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                    )
                                ),
                                no=Node(
                                    question="Is the pain on the top of the wrist?",
                                    yes=Node(
                                        recommendation="Left top wrist exercises",
                                        instructions="To perform Left top wrist exercises:\n1. Sit with your left arm extended and palm facing down.\n2. Use your right hand to gently pull back on your left fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                    ),
                                    no=Node(
                                        recommendation="Left bottom wrist exercises",
                                        instructions="To perform Left bottom wrist exercises:\n1. Sit with your left arm extended and palm facing up.\n2. Use your right hand to gently pull back on your left fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                    )
                                )
                            ),
                            no=Node(
                                question="Is the pain in the elbow?",
                                yes=Node(
                                    question="Is the pain in the right elbow?",
                                    yes=Node(
                                        question="Is the pain on the inner side of the elbow?",
                                        yes=Node(
                                            recommendation="Right inner elbow exercises",
                                            instructions="To perform Right inner elbow exercises:\n1. Sit with your right arm extended and palm facing up.\n2. Use your left hand to gently pull back on your right fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                        ),
                                        no=Node(
                                            recommendation="Right outer elbow exercises",
                                            instructions="To perform Right outer elbow exercises:\n1. Sit with your right arm extended and palm facing down.\n2. Use your left hand to gently pull back on your right fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                        )
                                    ),
                                    no=Node(
                                        question="Is the pain on the inner side of the elbow?",
                                        yes=Node(
                                            recommendation="Left inner elbow exercises",
                                            instructions="To perform Left inner elbow exercises:\n1. Sit with your left arm extended and palm facing up.\n2. Use your right hand to gently pull back on your left fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                        ),
                                        no=Node(
                                            recommendation="Left outer elbow exercises",
                                            instructions="To perform Left outer elbow exercises:\n1. Sit with your left arm extended and palm facing down.\n2. Use your right hand to gently pull back on your left fingers.\n3. Hold for 20 seconds.\n4. Repeat 5 times."
                                        )
                                    )
                                ),
                                no=Node(
                                    question="Is the pain in the neck?",
                                    yes=Node(
                                        question="Is the pain radiating to the shoulders?",
                                        yes=Node(
                                            recommendation="Neck to shoulder pain exercises",
                                            instructions="To perform Neck to shoulder pain exercises:\n1. Sit comfortably with your back straight.\n2. Tilt your head towards one shoulder.\n3. Hold for 20 seconds.\n4. Repeat on the other side.\n5. Do this 5 times."
                                        ),
                                        no=Node(
                                            recommendation="Neck pain exercises",
                                            instructions="To perform Neck pain exercises:\n1. Sit comfortably with your back straight.\n2. Slowly turn your head to one side as far as you can.\n3. Hold for 10 seconds.\n4. Repeat on the other side.\n5. Do this 5 times."
                                        )
                                    ),
                                    no=Node(
                                        recommendation="Consult a specialist",
                                        instructions="It is recommended to consult a specialist for further diagnosis and treatment."
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    return tree

def traverse_tree(node, answers):
    if node.recommendation is not None:
        return {'recommendation': node.recommendation, 'instructions': node.instructions}
    question = node.question
    answer = answers.get(question)
    if answer == "yes":
        return traverse_tree(node.yes, answers)
    elif answer == "no":
        return traverse_tree(node.no, answers)
    else:
        return {'question': question}

def get_next_step(answers):
    tree = build_tree()
    return traverse_tree(tree, answers)
