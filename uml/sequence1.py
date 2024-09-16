from plantuml import PlantUML

# Specify the PlantUML server URL
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')


uml_code = """
@startuml
' Define common entities with aliases
participant "Student" as s
participant "Tutor" as t
participant "Administrator" as admin
participant "GUI/App" as gui
participant "Webservice" as ws
participant "Database" as db
participant "Local Storage" as ls

' Student View
alt Student View
    s -> gui: Enter login credentials
    gui -> ws: Send credentials to webservice
    ws -> db: Check credentials in database
    db --> ws: Authorization success
    ws --> gui: Return confirmation
    gui --> s: Display login success
    s -> ls: Save session token in local storage
end

' Tutor View
alt Tutor View
    t -> gui: Enter login credentials
    gui -> ws: Send credentials to webservice
    ws -> db: Check credentials in database
    db --> ws: Authorization success
    ws --> gui: Return confirmation
    gui --> t: Display login success
    t -> ls: Save session token in local storage
end

' Administrator View
alt Administrator View
    admin -> gui: Enter login credentials
    gui -> ws: Send credentials to webservice
    ws -> db: Check credentials in database
    db --> ws: Authorization success
    ws --> gui: Return confirmation
    gui --> admin: Display login success
    admin -> ls: Save session token in local storage
end
@enduml

"""

with open('sequence_diagram.txt', 'w') as f:
    f.write(uml_code)

# Generate the diagram
plantuml.processes_file('sequence_diagram.txt')

















# from plantuml import PlantUML

# # Specify the PlantUML server URL
# plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# # Define the sequence diagram with opt and loop
# # uml_code = """
# # @startuml
# # Faculty -> GUI: Login()
# # opt Optional message
# #     Faculty --> GUI: I was waiting for your message!
# # end

# # loop 5 times
# #     Alice -> Bob: Ping
# #     Bob --> Alice: Pong
# # end

# # Alice -> Bob: Goodbye!
# # @enduml
# # """
# uml_code = """
# @startuml
# participant "Student" as s
# participant "Instructor" as i
# participant "System" as sys

# s -> sys: Submit Assignment
# sys --> s: Confirmation

# i -> sys: Grade Assignment
# sys --> i: Submission List
# i -> s: Return Graded Assignment

# s -> i: Ask for clarification
# i --> s: Provide explanation
# @enduml
# """

# # Write the UML code to a .txt file (optional)
# with open('sequence_diagram.txt', 'w') as f:
#     f.write(uml_code)

# # Generate the diagram
# plantuml.processes_file('sequence_diagram.txt')





