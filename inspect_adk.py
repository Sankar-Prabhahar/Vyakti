import pkgutil
import google.adk
import google.adk.agents

print("Modules in google.adk:")
for loader, module_name, is_pkg in pkgutil.walk_packages(google.adk.__path__, google.adk.__name__ + "."):
    print(module_name)

print("\nAttributes of LlmAgent:")
from google.adk.runners import Runner
from google.adk.tools import google_search

print("\nAttributes of Runner:")
print(dir(Runner))

print("\nType of google_search:")
print(type(google_search))
print(dir(google_search))
