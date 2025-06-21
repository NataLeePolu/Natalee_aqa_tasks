import pytest
from hw16_1 import TeamLead

def test_teamlead_attributes():
    lead = TeamLead(name="Alice", salary=100000, department="Backend", programming_language="Java")

    assert hasattr(lead, "department"), "TeamLead should have 'department' attribute"
    assert hasattr(lead, "programming_language"), "TeamLead should have 'programming_language' attribute"

    print("✅ All additional attributes are present in TeamLead.")

test_teamlead_attributes()