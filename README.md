# 2020-software-engineering-projects-pk
starter pk modelling repository

#Status update Friday:
- We finished the protocol.py and main.py files so that you can run 
protocols with input parameters from the config yaml file, or from the 
command line.
- We completed some unit test (unit testing for the rhs function in the 
model class does not work yet) and attempted to use codecov, but since 
some tests do not work, this would be a future step 


#Status update Thurs afternoon: 
- We are implementing the system of classes for different model types. 
- Discussed different methods of dosing (ie linear incrimental) and implemented that 
(while keeping default single dose option)
 
#Status update Thurs morning: 
- We discussed the best structure to have protocol separate from the model(with 1 
compartment and 2 compartment models separate), and to 
separate/specify the types of dosing (sub and ib). After trying out a few ideas, we are 
going forward with making classes for 1 vs 2 compartments (for 1, we simply set 
arguments for the peripheral compartment default to 0). Then, we also have sub and ib 
classes that inherit from these model classes. In the model parent classes, we have a 
function that determines ib vs sub. 


Features: 
- The ability to specify the form of the PK model, including the number of peripheral compartments, the type of dosing (intravenous bolus versus subcutaneous), and the dosing protocol. #Hew

- Users can specify the protocol independently from the model (e.g. be able to solve a one and two compartment model for the same dosing protocol) #Hew

- Ability to solve for the drug quantity in each compartment over time, 
given a model and a protocol #Sofia

- Ability to visualise the solution of a model, and to compare two different solutions. #Kingsley

- Put the 4 above into YAML 

- pip installable

- github repository, with issues + PRs that fully document the development process

- unit testing with a good test coverage

- fully documented, e.g. README, API documentation, OS license

- continuous integration (e.g. Github actions) for automatic testing and documentation generation
