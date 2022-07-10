IN_INNOVATION_DASH_YES = 'yes'
IN_INNOVATION_DASH_YES_NO_ID = 'yes_no_id'
IN_INNOVATION_DASH_DONT_KNOW = 'i_dnt_know'
IN_INNOVATION_DASH_NO = 'no'

IN_INNOVATION_DASH_CHOICES = (
    (IN_INNOVATION_DASH_YES, "Yes, provide the CGIAR Innovation Dashboard ID or Title of Innovation as answer"
                             " to the next question"),
    (IN_INNOVATION_DASH_YES_NO_ID, "Yes, but I cannot find the Innovation ID or Title of Innovation in the CGIAR"
                                   " Innovation Dashboard"),
    (IN_INNOVATION_DASH_DONT_KNOW, "I do not know"),
    (IN_INNOVATION_DASH_NO, "No, this innovation is not documented in the existing CGIAR Innovation Dashboard"),
)

CHARACTERIZATION_INCREMENTAL = 'incremental'
CHARACTERIZATION_RADICAL = 'radical'
CHARACTERIZATION_DISRUPTIVE = 'disruptive'
CHARACTERIZATION_OTHER = 'other'

CHARACTERIZATION_CHOICES = (
    (CHARACTERIZATION_INCREMENTAL, "Incremental innovation (constant, steady progress or improvement to existing "
                                   "innovations; aims at improving existing products, systems, processes, "
                                   "policies, etc.)"),
    (CHARACTERIZATION_RADICAL, "Radical innovation (new innovations that replace existing products, systems, "
                               "processes and policies)"),
    (CHARACTERIZATION_DISRUPTIVE, "Disruptive innovation (new innovations that cause/ require broader "
                                  "reconfiguration of the farming, market or policy systems and business models "
                                  "in which they are embedded)"),
    (CHARACTERIZATION_OTHER, "Other/ I’m not sure/ This characterization does not work for my innovation"),
)

TOPOLOGY_TECHNOLOGICAL = 'technological'
TOPOLOGY_CAPACITY_DVT = 'capacity_dvt'
TOPOLOGY_POLICY_MODEL = 'policy_or_model'
TOPOLOGY_OTHER = 'other'

TOPOLOGY_CHOICES = (
    (TOPOLOGY_TECHNOLOGICAL, "Technological innovation (e.g. varieties/ breeds; crop and livestock management "
                             "practices; machines; processing technologies; big data and information systems; etc.)"),
    (TOPOLOGY_CAPACITY_DVT, "Capacity development innovation (e.g. farmer, extension or investor decision-support "
                            "tools; farmer service provision model; training programs and curricula; online "
                            "courses; etc.)"),
    (TOPOLOGY_POLICY_MODEL, "Policy, organizational or institutional innovation (e.g. policy engagement strategies;"
                            " business models; policy arrangements; finance and regulatory mechanisms; partnership"
                            " models or mechanisms; public or private delivery strategies; etc.)"),
    (TOPOLOGY_OTHER, "Other/ I’m not sure/ This typology does not work for my innovation"),
)

YES_CHOICE_VALUE = 'yes'
NO_CHOICE_VALUE = 'no'

YES_NO_CHOICES = (
    (YES_CHOICE_VALUE, 'Yes'),
    (NO_CHOICE_VALUE, 'No'),
)