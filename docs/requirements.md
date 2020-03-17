# BOOTHROYD REQUIREMENTS

## Self-Hosting
   1a. Be able to self-host with these requirements

## Testing
   2a. Be able to link tests to requirements
   2b. Link requirements to individual commits where the test was introduced
   2c. Indicate to the user that a requirement has a test, and whether that test is passing
   2d. Tests are stored separate to requirements
   2e. Tests contain a description, a location, and the commit they were introduced

## Links to External Services
   3a. Be able to link to external services for each requirement
   3b. Each requirement must be able to link to multiple external services (e.g. multiple mantis URLs)

## User Stories
   4a. User stories should be able to be entered and stored separate to requirements
   4b. User stories should be able to be linked to multiple requirements

## Requirements
   5a. A requirement is composed of a description, a title, a date entered, a date first entered, an author
   5b. A requirement may be revised, and the history of revisions should be immutable
   5c. A requirement may be hierarchical, or link to other requirements
   5.c.a. A requirement may dependent, related-to, 
   5d. A requirement must be directed (i.e. has a parent) and a-cyclic (no cycles in the requirements graph)
   5d.a. The user interface must prevent the insertion of non-directed or cyclic requirements
