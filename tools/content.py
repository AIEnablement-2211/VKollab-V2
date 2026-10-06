"""Page content for the VKollab site.

Copy is grounded in the existing vkollab.com pages and the facts in FACTS below.
No clients, case studies, awards or certifications are claimed; add them in
home() under the "proof" section when they can be verified."""

# ---------------------------------------------------------------------------
# Service catalogue
# Each service: name, tag (one-line), description (meta), icon, diagram,
# problem, capability (list of (title, body)), approach (list of (title, body)),
# deliverables (list), outcomes (list of (title, body)), use_cases (list), related (slugs)
# ---------------------------------------------------------------------------
SERVICES = {
    "sap-application-development": {
        "name": "SAP Application Development",
        "tag": "Extend, integrate and build on SAP",
        "icon": "layers",
        "diagram": "development",
        "description": "Custom SAP application development: ABAP and Fiori extensions, integrations, data modernisation and cloud deployment of SAP workloads, delivered by VKollab's architects, consultants and QA specialists.",
        "intro": "Standard SAP covers most of a business. The remainder — the process that makes you different, the interface a partner insists on, the report the board actually reads — has to be built. We build it so that it survives the next upgrade.",
        "problem": "Organisations accumulate custom objects for good reasons and then pay for them at every release. Development done without an architecture view creates technical debt; development done without process knowledge creates software nobody uses. The work has to be anchored in both.",
        "capability": [
            ("Extensions and custom development", "ABAP and RAP-based enhancements, custom transactions, workflows, forms and reports that follow SAP's clean-core guidance so standard upgrades stay standard."),
            ("Integration", "Process-to-process and system-to-system integration between SAP, on-premise applications, cloud services and third-party platforms, using OData, IDoc, RFC and middleware connectors."),
            ("Data modernisation", "A modern data foundation and strategy for the SAP estate — master data quality, reporting models and the groundwork for analytics on HANA."),
            ("Cloud deployment", "Design and deployment of SAP applications and workloads on AWS, Google Cloud, Microsoft Azure or private cloud."),
            ("SAP Business One", "Licence procurement and installation, implementation and customisation, SQL-to-HANA migration, add-ons and upgrades for mid-sized organisations."),
        ],
        "approach": [
            ("Strategise", "Clarify the business objective, the budget, the timeline and the deliverables before any code is written, so that every stakeholder shares the same definition of done."),
            ("Execute", "Configure and build with tested implementation methods, in sprints that keep disruption to live operations to a minimum and surface risk early."),
            ("Elevate", "Stay through the transition from project to live operation — hypercare, knowledge transfer and continuous support while teams climb the learning curve."),
        ],
        "deliverables": ["Solution design and technical specification", "Developed and unit-tested objects, transported through the landscape", "Integration specifications and interface monitoring set-up", "Test scripts, UAT support and cut-over plan", "Operations handbook and knowledge transfer"],
        "outcomes": [
            ("A cleaner core", "Custom code that is documented, separated from standard where possible, and ready for the next release."),
            ("Processes that fit", "Software shaped around how the business actually works rather than the other way round."),
            ("Faster change later", "A development baseline — standards, naming, transport discipline — that makes subsequent work cheaper."),
            ("One team across modules", "Developers who understand how FI, MM, SD and PP interrelate, so changes in one area do not break another."),
        ],
        "use_cases": ["Separating a single SAP ERP instance into distinct instances aligned to different business units", "Building partner-facing interfaces on top of standard order-to-cash", "Replacing spreadsheet-driven sub-processes with governed SAP transactions"],
        "related": ["sap-fiori-ui5", "sap-migration-upgrades", "sap-application-management"],
    },
    "sap-migration-upgrades": {
        "name": "SAP Migration & Upgrades",
        "tag": "Move releases, databases and platforms safely",
        "icon": "migrate",
        "diagram": "migration",
        "description": "SAP migration and upgrade services from operating system to database to application: release upgrades, enhancement packages, HANA migrations, RISE with SAP workload moves and integration across the landscape.",
        "intro": "An SAP upgrade or migration touches the operating system, the database, the application and every custom object and interface in between. We plan and run the whole stack as one programme, with the business impact measured before the first system is touched.",
        "problem": "Upgrades are deferred because they feel risky, and then become riskier because they were deferred. Enhancement packages, support packs, add-ons and database changes pile up; custom code and interfaces are undocumented; downtime windows are scarce. The result is a programme no one wants to own.",
        "capability": [
            ("Release upgrades and enhancement packages", "Major release changes, EHP application, support package stacks and add-on installation across ABAP and Java stacks."),
            ("Database and OS migration", "Heterogeneous migrations and moves to SAP HANA, with the operating system, database and application layers sequenced together."),
            ("Workload migration", "Moving the right workloads to the right platform — on-premise, hyperscaler or private cloud — including RISE with SAP engagements."),
            ("Integration", "Integration between processes and data, between on-premise and cloud applications, and with external third-party systems; custom SAP connectors where standard ones fall short."),
        ],
        "approach": [
            ("Technical assessment", "A defined view of the current landscape: systems, custom objects, interfaces and the specific risks of introducing HANA or a new release into it, with a next-steps plan."),
            ("Solution assessment", "A solution blueprint with business and technical requirements and the proposed target architecture, developed with your IT team."),
            ("Technical upgrade", "Execution across operating systems, databases and ABAP objects — reports, function pools, interfaces and custom developments — from source to target, with testing to keep business impact minimal."),
            ("Implementation and hypercare", "Integration with the existing infrastructure, data integration, HANA data modelling and loading, front-end build and post-go-live support."),
        ],
        "deliverables": ["Landscape and custom-code assessment report", "Target architecture and migration runbook", "Downtime plan and rollback procedure", "Regression test plan and results", "Post-migration optimisation recommendations"],
        "outcomes": [
            ("Faster time to value", "Accelerators and a reviewed set of recommended settings shorten the path from decision to productive system."),
            ("Mission-critical certainty", "Risks identified and mitigated before cut-over; the technology estate evaluated for the capacity to support the change with minimal downtime."),
            ("One accountable team", "Operating system, database, application and integration handled by a single team rather than three vendors."),
            ("A platform for what is next", "Each migration lays the foundation for future projects instead of becoming the next one."),
        ],
        "use_cases": ["Moving an ECC system to HANA ahead of an S/4HANA conversion", "Upgrading SAP Business One to the latest version without business disruption", "Consolidating multiple interfaces during a platform move"],
        "related": ["sap-s4hana", "sap-application-management", "sap-application-development"],
    },
    "sap-application-management": {
        "name": "SAP Application Management",
        "tag": "Run, support and continuously improve SAP",
        "icon": "shield",
        "diagram": "management",
        "description": "SAP Application Management Services (AMS): monitoring, functional and technical support, enhancements, patching, upgrades, backup and recovery and help-desk, with SAP Solution Manager as the operating backbone.",
        "intro": "Once SAP is live, the real cost begins. Our application management service takes accountability for keeping the landscape stable, current and improving — so your own team can spend its time on the business rather than on tickets.",
        "problem": "In-house SAP teams are stretched between keeping the lights on and delivering change. Patches slip, audits find gaps, and institutional knowledge sits with a handful of people. Total cost of ownership rises quietly.",
        "capability": [
            ("Monitoring and administration", "Proactive, automated monitoring of systems, databases and interfaces, with administration by experienced SAP resources."),
            ("Functional and technical support", "Incident, problem and request handling across modules; help-desk services with the option of local-language support."),
            ("Enhancements and small change", "A steady channel for improvements and new functionality, deployed and maintained as part of the service."),
            ("Patch, upgrade and security", "Smart patch management, database management, upgrades and routine application and database security audits for vulnerabilities and non-compliance."),
            ("Backup, recovery and continuity", "Backup and recovery procedures tested, documented and aligned to business continuity requirements."),
        ],
        "approach": [
            ("Transition", "Knowledge capture, access, tooling and runbooks established before the service starts; SAP Solution Manager configured as the ALM platform."),
            ("Stabilise", "Reduce the incident backlog, fix recurring root causes and put monitoring in place so problems are seen before users report them."),
            ("Optimise", "Regular system tuning, TCO reviews and a visible enhancement pipeline reviewed with your business owners."),
            ("Scale", "Flexible contracting that lets you scale SAP resources up or down as requirements change, with guaranteed uptime targets."),
        ],
        "deliverables": ["Service catalogue and SLA definitions", "Monitoring dashboards and alerting", "Monthly service reports with incident and change metrics", "Audit findings and remediation log", "Enhancement backlog and release calendar"],
        "outcomes": [
            ("Lower total cost of ownership", "Maintenance costs fall as dedicated technical and functional assistance replaces ad-hoc effort and lets internal resources focus on higher-value work."),
            ("Stability and uptime", "Proactive monitoring, patching and tuning reduce security incidents and unplanned downtime."),
            ("Agility", "A standing team that can absorb new business requirements without a fresh procurement each time."),
            ("Audit readiness", "Routine audits and documented controls mean inspections become a formality."),
        ],
        "use_cases": ["Taking over support of a landscape after the original implementer rolls off", "Running 24/7 coverage across US and Indian time zones", "Managing S/4HANA after conversion while the business absorbs the change"],
        "related": ["sap-migration-upgrades", "sap-s4hana", "sap-application-development"],
    },
    "sap-s4hana": {
        "name": "SAP S/4HANA",
        "tag": "Conversion, implementation and in-memory simplification",
        "icon": "core",
        "diagram": "s4hana",
        "description": "SAP S/4HANA services: landscape sizing, migration strategy and path selection, data clean-up, conversion or new implementation, and post-go-live adoption, using HANA's in-memory platform to simplify business processes.",
        "intro": "S/4HANA replaces batch-run dependencies with real-time processing on an in-memory database. Done well, it removes layers of complexity from finance, logistics and manufacturing. Done badly, it moves old problems to a more expensive platform. The difference is in the preparation.",
        "problem": "Many organisations know they must move to S/4HANA but not how: greenfield or conversion, which deployment option, how much data to carry, how to size infrastructure, and how to keep the business running during the change.",
        "capability": [
            ("Landscape assessment and sizing", "Careful sizing of the S/4HANA infrastructure — the most consequential step in the technical project plan — covering landscape design, hardware and infrastructure."),
            ("Migration strategy", "Pre-migration planning, choosing the right migration path (new implementation, system conversion or selective data transition), selecting deployment options and sequencing post-migration activities."),
            ("Data reduction and cleansing", "Reducing data volume so that only essential data is migrated, shortening relocation time and lowering risk."),
            ("Implementation and conversion", "Execution of the chosen path, including custom-code adaptation, Fiori activation and integration re-pointing."),
            ("Manufacturing and quality", "S/4HANA Manufacturing for planning and scheduling and for production engineering and operations; quality management with predictive insight into losses from quality issues."),
            ("Analytics on HANA", "Real-time, enterprise-wide analytics on the in-memory platform — including integration with data platforms such as Hadoop."),
        ],
        "approach": [
            ("Set expectations", "Align objectives with business goals and set elevated expectations for every stage, from preparation to migration — a productive programme is one where nothing is left vague."),
            ("Prepare", "Readiness checks, custom-code analysis, data archiving and clean-up, and a sized target landscape."),
            ("Convert or implement", "Sandbox, development, quality and production cycles with full regression testing and dress rehearsals of the cut-over."),
            ("Adopt", "Hypercare, user enablement and a roadmap for the S/4HANA capabilities you did not switch on at go-live."),
        ],
        "deliverables": ["Readiness and sizing report", "Migration path recommendation with cost and risk comparison", "Data reduction plan", "Converted or implemented S/4HANA system with test evidence", "Adoption roadmap"],
        "outcomes": [
            ("Budget predictability", "Integrated project dashboards give full visibility into outcomes, workflows, deadlines and data quality."),
            ("Optimised data quality", "Data integrity and strategic alignment that leaders can make decisions on."),
            ("Increased efficiency", "A migration approach that simplifies, speeds up and de-risks each transfer wave beyond conventional ETL."),
            ("Accelerated future value", "Knowledge about your teams, roles, processes, data rules and mappings is captured for reuse in future initiatives."),
        ],
        "use_cases": ["ECC to S/4HANA system conversion with a reduced data footprint", "Centralising hardware and network resources on a single HANA platform", "Enabling real-time quality analytics across plants"],
        "related": ["sap-migration-upgrades", "sap-eppds", "sap-fiori-ui5"],
    },
    "sap-fiori-ui5": {
        "name": "SAP UI5/FIORI",
        "tag": "Role-based user experiences for SAP",
        "icon": "window",
        "diagram": "fiori",
        "description": "SAP Fiori and SAPUI5 development: custom Fiori applications, UI5 apps, extensions to standard Fiori apps, and ongoing support, built with SAP Gateway, OData, Workflow and ABAP.",
        "intro": "Most of what people do in SAP every day — approvals, look-ups, self-service tasks — should take seconds, on any device. Fiori and UI5 are how that happens. We build applications that follow Fiori design principles where it matters and depart from them only when the business case says so.",
        "problem": "Users avoid SAP transactions that were designed for a different era, and work around them in email and spreadsheets. Adoption suffers, data quality suffers, and the investment in the core is undercut at the point of use.",
        "capability": [
            ("Custom Fiori application development", "Applications tailored to your processes using SAP Gateway, SAPUI5, SAP Workflow and ABAP, with enhanced usability and functionality."),
            ("SAPUI5 development", "Responsive UI5 applications that run across devices and platforms, built on the UI5 framework and its control library."),
            ("Fiori app extensions", "Extending and enhancing standard Fiori applications so they align with your processes without losing the upgrade path."),
            ("Launchpad and role design", "Fiori Launchpad configuration, catalogues, groups and roles, so each user sees the apps relevant to their job."),
            ("Support and maintenance", "Keeping Fiori and UI5 applications current with SAP updates and enhancements."),
        ],
        "approach": [
            ("Understand the role", "Start from who does the task, how often, and on what device — not from the transaction code."),
            ("Design against Fiori guidelines", "Apply SAP's design principles and concept so applications feel consistent with standard Fiori; deviate deliberately, not accidentally."),
            ("Build and test with users", "Short cycles with real users and real data, with quality assurance throughout so the final product matches the business goal."),
            ("Operate", "Performance monitoring, OData service management and a maintenance plan."),
        ],
        "deliverables": ["UX review and app inventory", "Wireframes and interaction specifications", "Developed Fiori/UI5 applications and OData services", "Launchpad configuration and role mapping", "Support and maintenance plan"],
        "outcomes": [
            ("Adoption", "Interfaces people choose to use, which is the only way the data in SAP stays accurate."),
            ("Mobility", "Approvals and look-ups that work on a phone in a warehouse or an airport."),
            ("Consistency", "One design language across custom and standard applications."),
            ("Upgrade safety", "Extensions built in supported ways survive SAP's release cycle."),
        ],
        "use_cases": ["Replacing paper or email approvals with Fiori workflow apps", "Partner or supplier self-service portals on UI5", "Shop-floor confirmations on tablets"],
        "related": ["sap-application-development", "sap-s4hana", "sap-application-management"],
    },
    "sap-ibp": {
        "name": "SAP Integrated Business Planning",
        "tag": "S&OP, demand, inventory, response and supply",
        "icon": "chart",
        "diagram": "ibp",
        "description": "SAP IBP consulting and implementation: strategy and business case, process design, S&OP, demand planning, inventory optimisation and response and supply planning, with integration, training and ongoing support.",
        "intro": "Shifting markets and fragile supply chains have made planning a continuous activity rather than a monthly ritual. SAP IBP gives planning teams a single, cloud-based model for sales and operations, demand, inventory and supply. We bring both the SAP knowledge and the supply-chain process experience to make it work.",
        "problem": "Planning is split across spreadsheets, legacy APO instances and departmental tools. Demand, supply and finance do not reconcile; forecasts are stale by the time they are reviewed; inventory is held in the wrong places; and disruption is handled by phone.",
        "capability": [
            ("IBP strategy", "Deciding whether SAP IBP is right for your business, building the business case and shaping the roadmap."),
            ("Process and organisational design", "Process assessment and design, process harmonisation, organisational alignment, and KPI, reporting and analytics capabilities — because technology alone does not deliver the benefit."),
            ("Implementation", "Functional consulting, integration, programme and project management, testing, master data and reporting, training and change management."),
            ("Sales & Operations Planning", "A cross-functional master plan that balances demand and supply, aligns supply-chain plans with financial objectives, surfaces constraints and exceptions, and simulates scenarios with escalation options for management."),
            ("Demand planning", "Medium- to long-term forecasting with advanced statistical models, role-specific local and central planning, manual overrides, predecessor–successor (PLM) relationships, promotions and global collaboration."),
            ("Inventory optimisation", "Multi-stage optimisation across the whole network and all BOM levels using stochastic algorithms; what-if analysis on safety stock and capital commitment; strategic stock placement to reduce the bullwhip effect."),
            ("Response and supply", "Time-series tactical planning with capacity expansion, component substitution and multi-sourcing; order-based operational planning with rule-based prioritisation linked to ATP; reactive rescheduling of production, distribution and procurement orders."),
        ],
        "approach": [
            ("Value discovery", "Quantify where better planning changes the P&L — forecast accuracy, inventory, service level — and agree the scope."),
            ("Design", "Planning areas, key figures, master data and the S&OP cadence designed with the planners who will own them."),
            ("Build and integrate", "Configuration, integration with S/4HANA or ECC, data loads and validation against historic plans."),
            ("Adopt and improve", "Training, change management and ongoing support as planning matures from monthly to continuous."),
        ],
        "deliverables": ["Business case and roadmap", "Process and KPI design", "Configured IBP planning areas and integration", "Training material and cut-over plan", "Ongoing support model"],
        "outcomes": [
            ("Forecast accuracy", "Statistical and customer forecasts combined, harmonised across local and global planning."),
            ("Lower inventory", "Safety stock set by optimisation rather than habit, placed where it protects service."),
            ("Customer satisfaction", "Confirmed orders that reflect real supply, and faster response when the network changes."),
            ("One plan", "Demand, supply and finance working from the same numbers in the same cadence."),
        ],
        "use_cases": ["Replacing APO demand planning with IBP for Demand", "Introducing a monthly S&OP cycle across regions", "Setting multi-echelon safety stock for a global network"],
        "related": ["sap-eppds", "sap-s4hana", "sap-advanced-track-trace"],
    },
    "sap-eppds": {
        "name": "SAP ePPDS",
        "tag": "Embedded production planning and detailed scheduling",
        "icon": "schedule",
        "diagram": "eppds",
        "description": "SAP embedded PP/DS (ePPDS) in S/4HANA: finite production planning and detailed scheduling against resource capacity, heuristics and optimisers, alert monitoring and integration with IBP and the S/4HANA core.",
        "intro": "ePPDS is the planning and scheduling engine embedded in S/4HANA. It plans production in detail against real resource capacity — bottlenecks, set-ups, sequences — rather than assuming infinite capacity and finding out otherwise on the shop floor.",
        "problem": "Companies with complex processes, bottleneck resources and tight lead times cannot plan with MRP alone. Schedules are rebuilt by hand, capacity is discovered late, and expediting becomes the operating model.",
        "capability": [
            ("Detailed planning", "Planning of production that considers material requirements and resource capacities together."),
            ("Resource optimisation", "Scheduling that optimises resource utilisation to meet customer demand with shorter lead times."),
            ("Capacity planning", "Resource capacities and constraints respected during planning, not after."),
            ("Heuristics and optimisers", "Standard and tailored heuristics and optimisers to find workable, cost-aware plans and sequences."),
            ("Alert monitoring", "An alert monitor that surfaces exceptional, unexpected or critical situations in the plan so planners act on exceptions."),
            ("Integration", "Embedded in S/4HANA, with integration to IBP for tactical plans and to shop-floor execution."),
        ],
        "approach": [
            ("Value discovery", "Identify the plants, lines and products where finite scheduling changes throughput or lead time."),
            ("Model design", "Resources, PPMs/PDS, set-up matrices, planning procedures and heuristics designed with planners and production."),
            ("Build and validate", "Configuration in S/4HANA, validated against historic orders and known bottleneck weeks."),
            ("Operate", "Planner training, alert handling routines and ongoing support as the model is extended to more lines."),
        ],
        "deliverables": ["Scope and value assessment by plant", "Planning model design document", "Configured ePPDS with heuristics and alert profiles", "Planner playbook and training", "Support and enhancement plan"],
        "outcomes": [
            ("Improved resource utilisation", "Capacities and constraints are respected in the plan, so lines run to a schedule that is achievable."),
            ("Better customer service", "Realistic schedules improve on-time delivery and reduce lead times."),
            ("Reduced costs", "Less inventory, fewer capacity surprises and fewer production delays."),
            ("Better decisions", "Planners work from alerts and scenarios rather than from spreadsheets rebuilt every morning."),
        ],
        "use_cases": ["Finite scheduling on a bottleneck packaging line", "Sequence optimisation to reduce changeovers in process manufacturing", "Linking IBP supply plans to executable production schedules"],
        "related": ["sap-ibp", "sap-s4hana", "sap-application-management"],
    },
    "sap-advanced-track-trace": {
        "name": "SAP Advanced Track & Trace",
        "tag": "Pharmaceutical serialization and regulatory reporting",
        "icon": "barcode",
        "diagram": "attp",
        "description": "SAP Advanced Track and Trace for Pharmaceuticals (ATTP): serialization, aggregation, country-specific regulatory reporting (including DSCSA), multi-instance landscapes, and integration with ERP and supply-chain partners.",
        "intro": "Serialization sits at the intersection of international regulation, IT and logistics. SAP ATTP is the end-to-end platform pharmaceutical manufacturers use to serialise products, aggregate packaging levels and report to authorities. Our ATTP specialists implement and run it, and speak to regulators on your behalf when needed.",
        "problem": "Every market has its own serialization and reporting rules, and they keep changing. Manufacturers must validate products, integrate serialization with warehouse and order processes, exchange EPCIS data with partners, and keep audit-ready records — without slowing the line.",
        "capability": [
            ("Serialization and aggregation", "Serial number management, trade item and range management, packaging hierarchies (unit, case, pallet) and automated range requests for externally managed items."),
            ("Regulatory reporting", "Country-ready reporting packages — including attributes required for US DSCSA supply-chain reports — and protection from changing legislation through country packs."),
            ("Landscape design", "Standalone ATTP or ATTP as an extension to SAP ERP; multi-instance landscapes with queuing, alerting and control logic for distributed data, and RFC access for external systems to request EPCIS messages."),
            ("Warehouse and rework", "Web UI capabilities for warehouse-based transactions, batch decommissioning by scanned serial, unpack and single-serial decommissioning."),
            ("Integration", "Integration with SAP ECC/S/4HANA, line-level systems, 3PLs and wholesalers, with data cockpit configuration for customer-specific queries and change logs."),
        ],
        "approach": [
            ("Discovery and evaluation", "Markets, products, packaging levels and partner landscape mapped against current and upcoming regulation."),
            ("Design and validation planning", "Solution design with GxP validation deliverables planned from the start, not retrofitted."),
            ("Implementation", "Configuration, master data set-up, integration and validated testing against regulatory report formats."),
            ("Run and extend", "Ongoing support, new country packs as legislation changes, and enhancements such as archiving and location/business-partner integration improvements."),
        ],
        "deliverables": ["Regulatory and landscape assessment", "Validated solution design and traceability matrix", "Configured ATTP with integrations and country packs", "Validation evidence (IQ/OQ/PQ support)", "Support model and regulatory watch"],
        "outcomes": [
            ("Compliance across markets", "Country-ready reporting that keeps pace with legislation."),
            ("A secure supply chain", "Serialised, aggregated product that can be verified at every hand-off, supporting the fight against counterfeiting and illicit trade."),
            ("Lower maintenance cost", "A single SAP-integrated platform instead of point solutions per market."),
            ("Patient safety", "Indirectly, the point of all of it."),
        ],
        "use_cases": ["Implementing DSCSA-compliant reporting for the US market", "Consolidating multiple regional serialization systems onto ATTP", "Adding warehouse rework capability in a local ATTP instance"],
        "related": ["compliancewire", "sap-s4hana", "sap-application-management"],
    },
    "sap-successfactors": {
        "name": "SAP SuccessFactors",
        "tag": "Cloud HCM — core HR, payroll and talent",
        "icon": "people",
        "diagram": "successfactors",
        "description": "SAP SuccessFactors implementation and support: Employee Central core HR and payroll, Recruiting and Onboarding, Performance and Goals, learning and succession, with integration to S/4HANA and third-party systems.",
        "intro": "SuccessFactors is SAP's cloud Human Capital Management suite, built around the idea of Human Experience Management: HR processes designed from the employee's point of view. We implement and support it for organisations that want one platform from hire to retire.",
        "problem": "HR data is fragmented across payroll providers, spreadsheets and legacy systems. Managers cannot see their teams, employees cannot serve themselves, and compliance across countries is handled by hand.",
        "capability": [
            ("Employee Central", "Centralised employee data and organisational structures, automated HR processes with global compliance support, and payroll, time and attendance."),
            ("Recruiting and Onboarding", "A seamless candidate and recruiter experience and simplified onboarding that gets new hires productive sooner."),
            ("Performance and Goals", "Goals aligned to business objectives, continuous feedback, agile performance reviews and transparent career development paths."),
            ("Learning and succession", "Learning tied to skills and goals; succession pipelines built by identifying and developing high-potential talent."),
            ("Integration", "Integration with S/4HANA, payroll providers, identity and benefits platforms."),
        ],
        "approach": [
            ("Discover", "Current HR processes, data sources, countries and compliance requirements mapped against the SuccessFactors module set."),
            ("Configure", "Iterative configuration workshops per module, with data migration rehearsed early."),
            ("Integrate and test", "Interfaces to ERP, payroll and identity built and tested end to end, including parallel payroll runs where relevant."),
            ("Launch and support", "Change management, manager and employee enablement, and ongoing release management across SAP's half-yearly updates."),
        ],
        "deliverables": ["Process and module scope", "Configuration workbooks", "Data migration and integration specifications", "Test evidence and cut-over plan", "Release management and support model"],
        "outcomes": [
            ("Engagement and retention", "Employees who can see their goals, feedback and career path."),
            ("Streamlined HR and payroll", "Fewer manual steps and errors across countries."),
            ("Future-ready skills", "Learning and succession connected to the business plan."),
            ("Digital HR at scale", "One platform that grows with the organisation."),
        ],
        "use_cases": ["Banking and financial services: compliance and global talent management", "Healthcare and life sciences: workforce scheduling and growth", "Manufacturing: global payroll and shift-based workforces", "Retail: seasonal hiring and engagement", "Education and public sector: large-scale workforce planning"],
        "related": ["workday", "compliancewire", "sap-s4hana"],
    },
    "workday": {
        "name": "Workday",
        "tag": "Cloud HCM and Workday integrations",
        "icon": "cloud",
        "diagram": "workday",
        "description": "Workday HCM services: core HR and workforce management, payroll, time and absence, learning, performance and career growth, and Workday integrations using Studio, Cloud Connect, EIB and Workday Web Services.",
        "intro": "Workday Human Capital Management centralises workforce management in one cloud platform. Much of the value — and most of the difficulty — lies in how it connects to everything else: payroll, benefits, recruiting, ERP. That is where we spend most of our time.",
        "problem": "Workday is adopted for a flexible, unified HR experience, then surrounded by brittle integrations built under deadline pressure. Data drifts between systems, IT becomes a bottleneck for every change, and the real-time picture Workday promised never materialises.",
        "capability": [
            ("Core HR and workforce management", "Centralised employee records and organisational data; job profiles, compensation structures and workforce planning; self-service for employees and managers."),
            ("Payroll, time and absence", "Automated payroll with accuracy and compliance, integrated time tracking and scheduling, global payroll and regional compliance."),
            ("Learning, performance and career growth", "Personalised training tied to skills and goals, continuous feedback, and succession pipelines for high-potential talent."),
            ("Workday Studio integrations", "Complex, enterprise-grade integrations with high-volume data transfers, orchestration and customisation beyond standard connectors."),
            ("Cloud Connect and EIB", "Pre-packaged Cloud Connect integrations for payroll, benefits and recruiting; Enterprise Interface Builder for simple, file-based inbound and outbound integrations, scheduled or on demand."),
            ("Workday Web Services", "SOAP and REST APIs for real-time, system-to-system transactions and lightweight integrations with mobile apps, portals and third-party systems."),
        ],
        "approach": [
            ("Integration inventory", "Every interface catalogued by volume, frequency, direction and owner, and matched to the right Workday integration tool."),
            ("Design", "Low-code (EIB, Cloud Connect) where it fits, Studio where it does not; error handling and monitoring designed in."),
            ("Build and test", "Built against sandbox tenants with realistic data volumes and failure scenarios."),
            ("Operate", "Monitoring, release-impact review for each Workday update, and a change channel that does not require a project each time."),
        ],
        "deliverables": ["Integration inventory and tool mapping", "Integration design specifications", "Built and tested integrations with monitoring", "Runbooks and release-impact process", "Support model"],
        "outcomes": [
            ("Less manual HR administration", "Automated data exchange eliminates re-keying and the errors that come with it."),
            ("Real-time accuracy", "Payroll, benefits, ERP and recruiting platforms that agree with Workday."),
            ("Reduced IT dependency", "Low-code tools in the hands of HR and functional teams where appropriate."),
            ("Scalable, compliant integration", "An integration estate that supports enterprise volumes on a secure cloud architecture."),
        ],
        "use_cases": ["Connecting Workday to SAP S/4HANA finance for cost-centre and headcount data", "Replacing ad-hoc file transfers to a payroll provider with monitored EIB integrations", "Exposing Workday data to an internal portal through REST"],
        "related": ["sap-successfactors", "sap-application-development", "compliancewire"],
    },
    "compliancewire": {
        "name": "ComplianceWire",
        "tag": "Validated LMS administration for GxP organisations",
        "icon": "book",
        "diagram": "compliancewire",
        "description": "ComplianceWire LMS services for pharmaceutical, medical device and biologics companies: implementation and configuration, SCORM content development, ongoing administration, reporting and audit readiness, user training and help-desk.",
        "intro": "ComplianceWire is the cloud-based learning management system from UL Solutions used across pharmaceutical, medical device and biologics companies to deliver validated, GxP-compliant training. We implement, configure, administer and support it so that training records are complete the day an inspector asks.",
        "problem": "Regulated companies must prove that every person was trained on the current version of every procedure relevant to their role — with electronic signatures, audit trails and 21 CFR Part 11 and EU Annex 11 controls. Spreadsheets and generic LMS tools cannot carry that burden; a validated LMS can, if it is administered properly.",
        "capability": [
            ("Implementation and configuration", "Initial set-up aligned to your organisational structure, compliance requirements and SOPs: roles, user groups, hierarchy, curricula and certification paths."),
            ("Training content development", "SCORM-compliant learning modules tailored to your SOPs, policies and regulatory needs."),
            ("Ongoing administration", "User management, training assignments and day-to-day operation handled for you."),
            ("Reporting and audit readiness", "Dashboards and custom reports for complete visibility of completion rates and compliance gaps."),
            ("User training and help-desk", "Onboarding, administrator training and ongoing user support."),
            ("System integration", "Integration with HRIS, EDMS and other enterprise systems for user synchronisation, bulk uploads, historical data migration and REST-based data exchange."),
        ],
        "approach": [
            ("System set-up and landscape design", "Define roles, user groups and hierarchy clearly; align curricula and certification paths with business and compliance needs; integrate with HR systems for automatic user synchronisation."),
            ("Content strategy", "Upload only validated and approved materials; map training to job roles; review and update content on a schedule."),
            ("Compliance and data management", "Accurate training records for inspections, archiving and retention policies, and periodic audits of data integrity."),
            ("Adoption and continuous improvement", "Comprehensive onboarding, dashboard monitoring of completion and gaps, user feedback loops, and process updates as regulations evolve."),
        ],
        "deliverables": ["Configuration specification and role/curriculum matrix", "SCORM modules and content governance plan", "Integration specification (HRIS, EDMS)", "Audit-readiness dashboards and reports", "Administration runbook and support model"],
        "outcomes": [
            ("Audit-ready records", "Electronic signatures, audit trails and role-based training paths that satisfy 21 CFR Part 11 and EU Annex 11."),
            ("Training that follows the role", "Automated, role-based assignments so nobody is trained on the wrong procedure, or not at all."),
            ("Visibility", "Completion and overdue training visible to quality and line management in real time."),
            ("Capacity returned", "Administration taken off the quality team's desk."),
        ],
        "use_cases": ["Standing up ComplianceWire for a new manufacturing site", "Migrating historical training records from a legacy LMS", "Integrating LMS assignments with document control releases from an EDMS"],
        "related": ["sap-advanced-track-trace", "sap-successfactors", "workday"],
    },
}


def _merge(a, b, slug, name, tag, icon_name, diagram, description, intro, problem):
    A, B = SERVICES[a], SERVICES[b]
    return {
        "name": name, "tag": tag, "icon": icon_name, "diagram": diagram, "description": description, "intro": intro, "problem": problem,
        "capability": A["capability"][:4] + B["capability"][:4],
        "approach": A["approach"][:2] + B["approach"][:2],
        "deliverables": A["deliverables"][:3] + B["deliverables"][:3],
        "outcomes": A["outcomes"][:2] + B["outcomes"][:2],
        "use_cases": A["use_cases"][:2] + B["use_cases"][:2],
        "related": [],
    }


SERVICES["track-trace-compliancewire"] = _merge(
    "sap-advanced-track-trace", "compliancewire", "track-trace-compliancewire",
    "Advanced Track &amp; Trace + ComplianceWire", "Serialization and validated training for regulated industries", "barcode", "attp-cw",
    "SAP Advanced Track and Trace (ATTP) serialization and regulatory reporting, plus ComplianceWire LMS implementation and administration — the two systems regulated pharmaceutical, medical-device and biologics companies rely on.",
    "Two platforms built for regulated manufacturing. SAP Advanced Track &amp; Trace serialises product and reports to authorities; ComplianceWire keeps every person trained on the current version of every procedure. We implement and run both.",
    "Every market has its own serialization rules, and every inspector expects complete, validated training records. Point solutions per market and spreadsheet-tracked training cannot carry that burden; validated, SAP-integrated platforms can — if they are implemented and administered properly.",
)
SERVICES["sap-ibp-eppds"] = _merge(
    "sap-ibp", "sap-eppds", "sap-ibp-eppds",
    "SAP IBP + SAP ePPDS", "Integrated business planning and detailed production scheduling", "chart", "ibp-eppds",
    "SAP Integrated Business Planning (S&amp;OP, demand, inventory, response and supply) together with embedded PP/DS in S/4HANA for finite production planning and scheduling — one plan from the boardroom to the shop floor.",
    "IBP gives planning teams a single cloud model for sales and operations, demand, inventory and supply. Embedded PP/DS turns that tactical plan into an executable schedule against real resource capacity. We bring both the SAP knowledge and the supply-chain process experience to make the two work together.",
    "Planning is split across spreadsheets, legacy APO instances and departmental tools; schedules are rebuilt by hand because MRP assumes infinite capacity. Demand, supply and finance do not reconcile, and expediting becomes the operating model.",
)
SERVICES["sap-ai"] = {
    "name": "SAP AI", "tag": "AI and automation inside your SAP processes", "icon": "cloud", "diagram": "ai",
    "description": "SAP AI services: readiness assessment, SAP Business AI and Joule enablement, AI-assisted automation in finance, procurement, supply chain and HR processes, data foundations, and governance for responsible use.",
    "intro": "AI only pays off inside a business process. We help organisations apply SAP's AI capabilities — and complementary platforms — where they remove manual work, improve decisions and keep data governed, starting from the processes you already run on SAP.",
    "problem": "Organisations are asked to 'do something with AI' without a clear process to start from, clean data to feed it, or a governance model to trust it. Pilots multiply, few reach production, and the ones that do are hard to support.",
    "capability": [
        ("AI readiness and use-case discovery", "Workshops that map AI opportunities to your actual SAP processes, score them by value and feasibility, and set a roadmap."),
        ("SAP Business AI and Joule enablement", "Activation and configuration of SAP's embedded AI capabilities and the Joule assistant across S/4HANA, SuccessFactors and other SAP cloud applications where licensed."),
        ("Process automation", "AI-assisted automation in finance (cash application, invoice processing), procurement, supply-chain planning and HR, with human review built in."),
        ("Document and data intelligence", "Extraction, classification and validation of documents and master data feeding SAP, with exception handling routed to the right people."),
        ("Data foundation", "Master-data quality, integration and reporting models so AI capabilities have trustworthy inputs."),
        ("Copilot-style assistants", "Secure assistants for employees and support teams, grounded in your SAP data and documents, built on SAP BTP or Microsoft platforms as appropriate."),
        ("Governance and responsible use", "Access, audit, privacy and model-risk controls so AI features pass the same scrutiny as any other SAP change."),
    ],
    "approach": [
        ("Discover", "Identify the processes where AI removes the most manual effort or risk, and confirm the data exists to support them."),
        ("Prove", "A short, measured pilot inside one process with success criteria agreed up front."),
        ("Scale", "Harden the pilot: integration, monitoring, exception handling, training and transport into production."),
        ("Operate", "Run and improve under the same application-management model as the rest of your SAP estate."),
    ],
    "deliverables": ["AI opportunity map and roadmap", "Pilot design with success criteria", "Configured SAP AI capabilities and integrations", "Governance and control framework", "Operations runbook and enablement"],
    "outcomes": [
        ("Less manual work", "Repetitive, document-heavy steps handled by AI with people reviewing exceptions."),
        ("Better decisions, faster", "Forecasts, recommendations and anomalies surfaced inside the SAP screens people already use."),
        ("AI you can audit", "Controls and monitoring that satisfy internal audit and regulators."),
        ("A platform, not a pilot", "Capabilities that are supported and extended rather than abandoned."),
    ],
    "use_cases": ["Automating invoice and cash-application processing in S/4HANA finance", "AI-assisted demand forecasting feeding IBP", "An HR assistant grounded in SuccessFactors data and policy documents", "Master-data validation before it reaches the core"],
    "related": ["sap-s4hana", "sap-ibp-eppds", "sap-successfactors"],
}
for sl, rel in {
    "sap-application-development": ["sap-fiori-ui5", "sap-migration-upgrades", "sap-ai"],
    "sap-fiori-ui5": ["sap-application-development", "sap-s4hana", "sap-ai"],
    "sap-migration-upgrades": ["sap-s4hana", "sap-application-management", "sap-application-development"],
    "sap-s4hana": ["sap-migration-upgrades", "sap-ibp-eppds", "sap-ai"],
    "track-trace-compliancewire": ["sap-s4hana", "sap-successfactors", "sap-application-management"],
    "sap-ibp-eppds": ["sap-s4hana", "sap-ai", "sap-application-management"],
    "sap-application-management": ["sap-migration-upgrades", "sap-s4hana", "sap-ai"],
    "workday": ["sap-successfactors", "sap-application-development", "sap-ai"],
    "sap-successfactors": ["workday", "track-trace-compliancewire", "sap-ai"],
}.items():
    SERVICES[sl]["related"] = rel

INDUSTRIES = [
    {
        "slug": "pharma", "name": "Pharmaceutical & Life Sciences", "icon": "pill",
        "lede": "Serialization, regulatory reporting and validated training for pharmaceutical, medical device and biologics companies.",
        "body": "Two of our specialist practices exist because of this industry: SAP Advanced Track & Trace for serialization and country-specific reporting, and ComplianceWire for GxP training management. Both sit alongside the S/4HANA core, quality management and the supply-chain planning that keeps regulated product available.",
        "focus": ["Drug serialization and DSCSA / EU reporting", "GxP training with 21 CFR Part 11 controls", "Quality management on S/4HANA"],
        "services": ["track-trace-compliancewire", "sap-s4hana", "sap-ibp-eppds", "sap-ai"],
    },
    {
        "slug": "automotive", "name": "Automotive", "icon": "car",
        "lede": "OEMs and component manufacturers must sharpen today's core competencies while increasing the pace of innovation, integrating with technology partners and reshaping how they interact with end consumers.",
        "body": "Vehicles are becoming smarter and connected to a digital infrastructure, and buyers' expectations have moved with them. The underlying operations — multi-tier supply, engineering change, warranty, dealer networks — still have to run with precision. SAP S/4HANA gives automotive manufacturers enterprise-wide manufacturing collaboration and the real-time data to manage variant complexity, whether deployed on-premise or in the cloud.",
        "focus": ["Enterprise-wide manufacturing collaboration", "On-premise or cloud deployment", "Supplier integration and planning"],
        "services": ["sap-s4hana", "sap-ibp-eppds", "sap-application-management"],
    },
    {
        "slug": "manufacturing", "name": "Manufacturing", "icon": "factory",
        "lede": "S/4HANA Manufacturing for planning and scheduling, and for production engineering and operations, delivers a simplified user experience and enterprise-wide collaboration within one integrated environment.",
        "body": "Manufacturers gain insight into the quality aspects of their processes, streamline quality management and apply predictive algorithms to reduce losses from quality issues and recommend corrective action. Combined with embedded PP/DS for finite scheduling and IBP for the tactical plan, the result is a planning-to-execution chain that runs on one set of numbers.",
        "focus": ["Enriched, seamless digital manufacturing capabilities", "Real-time enterprise analytics for decision-making", "Finite scheduling against real capacity"],
        "services": ["sap-s4hana", "sap-ibp-eppds", "sap-fiori-ui5"],
    },
    {
        "slug": "logistics", "name": "Logistics & Transport", "icon": "truck",
        "lede": "Web and mobile solutions built for the transportation industry: fleet and cargo management, logistics software, dealer management platforms, travel planning and scheduling applications.",
        "body": "Transport businesses live on utilisation and visibility. We build and integrate the systems that keep fleets, cargo and schedules in view, connect them to the SAP core for finance and procurement, and design them to scale as networks grow.",
        "focus": ["Enhanced operational efficiency", "Scalable solutions for growth", "Integration between operational systems and SAP"],
        "services": ["sap-application-development", "sap-fiori-ui5", "sap-ibp-eppds", "sap-application-management"],
    },
    {
        "slug": "healthcare", "name": "Healthcare", "icon": "heart",
        "lede": "Healthcare ERP supports the daily operations behind patient care: appointments, accounting, human resources, procurement, project, risk and compliance management, supply chain and reporting.",
        "body": "Integrated with every core operation, a well-run ERP gives healthcare organisations straightforward planning, budget and cash-flow forecasting and performance reporting. We focus on user experience and decision support, and apply newer concepts — gamification, machine learning — only where they measurably improve adoption or outcomes.",
        "focus": ["Excellent user experience and decision support", "Planning, budgeting and cash-flow forecasting", "Workforce scheduling and growth with SuccessFactors"],
        "services": ["sap-s4hana", "sap-successfactors", "sap-fiori-ui5", "sap-application-management"],
    },
    {
        "slug": "banking", "name": "Banking & Financial Services", "icon": "bank",
        "lede": "SAP consulting for banking transformation in the USA and the UAE: streamlined operations, better customer experience and regulatory compliance.",
        "body": "Banks optimise processes, manage risk and stay compliant by integrating SAP's banking tools with automation and analytics. Our work covers SAP consulting for banking transformation, banking technology and automation, and the application of AI and machine learning capabilities within SAP where they improve operational efficiency and customer experience — including solutions shaped for the UAE market.",
        "focus": ["Reimagine business models to find new revenue and profit sources", "Converge information and operational technologies", "Compliance and global talent management with SuccessFactors"],
        "services": ["sap-s4hana", "sap-application-development", "sap-successfactors", "sap-application-management"],
    },
    {
        "slug": "real-estate", "name": "Real Estate & Infrastructure Construction", "icon": "blueprint",
        "lede": "ERP for infrastructure, residential and commercial construction and EPC businesses has to stay agile as requirements evolve while reflecting the legacy of how projects are actually run.",
        "body": "Three imperatives recur across construction and EPC: legal and statutory compliance, project estimation and cash flow, and control over subcontractors and materials across many sites. We configure SAP to handle project-based accounting and procurement and to give management a consolidated, current view of every project.",
        "focus": ["Legal and statutory compliance", "Project estimation and cash flow", "Multi-site procurement and subcontracting"],
        "services": ["sap-s4hana", "sap-application-development", "sap-fiori-ui5", "sap-application-management"],
    },
]


# ---------------------------------------------------------------------------
# Company facts used across pages. Verify before launch; change here only.
# ---------------------------------------------------------------------------
FACTS = [
    ("2020", "Founded"),
    ("4", "Offices: Parsippany NJ, Hyderabad, Guntur, Vijayawada"),
    ("90+", "SAP consultants and developers"),
    ("3", "Regions served: United States, Europe, Japan"),
]

VALUES = [
    ("Transparency", "Scope, risk and cost are stated plainly before work starts and reported honestly while it runs."),
    ("Integrity", "We recommend what the client needs, including when that is less work for us."),
    ("Long relationships", "The business is built on goodwill and repeat work. We work as an extension of the client's own team rather than as a vendor at arm's length."),
    ("Professional maturity", "Experienced people who stay calm under go-live pressure and keep their word on dates."),
]

WHY = [
    ("Regulated-industry depth", "Two of our practices exist for pharmaceutical and life-sciences clients: SAP Advanced Track &amp; Trace for serialization and DSCSA/EU reporting, and ComplianceWire for GxP training under 21 CFR Part 11. Few SAP partners of our size offer either."),
    ("One team from assessment to run", "The consultants who scope a programme stay through build, cut-over and hypercare, then run it under an SLA. Knowledge does not leave with the implementer."),
    ("Named consultants, US and India coverage", "Clients know who is on their account. Delivery centres in Hyderabad, Guntur and Vijayawada work alongside the New Jersey office, so support covers US business hours and overnight windows."),
    ("Clean-core discipline", "Custom development follows SAP's clean-core guidance and is documented and transported properly, so the next upgrade stays a standard upgrade."),
]

WORK_STEPS = [
    ("Assess", "Landscape, custom code, data and the business objective reviewed before any plan is committed. Output: a sized scope, risks and a cost range."),
    ("Design", "Solution blueprint, integration and data design, cut-over and test strategy, agreed with your IT and business owners."),
    ("Build and migrate", "Configuration, development and migration in controlled cycles with regression testing and dress rehearsals before go-live."),
    ("Run and improve", "Hypercare, knowledge transfer and then application management under an SLA with a visible enhancement pipeline."),
]

ENGAGEMENTS = [
    ("Fixed-scope project", "Assessment, implementation, migration or build with a defined scope, plan and acceptance criteria."),
    ("Managed service", "Application management under SLAs: monitoring, support, patching and enhancements with flexible capacity."),
    ("Extended team", "Named consultants and developers embedded with your team for a programme or a year, under your governance."),
    ("Advisory", "Short, senior engagements: migration path selection, landscape assessment, planning business case, serialization readiness."),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def hero(c, photo_key, tag, title, lede="", actions="", crumbs=None, tall=False, alt="", extra=""):
    crumb_html = c["breadcrumb"](crumbs) if crumbs else ""
    lede_html = f'<p class="lede lede--lg" data-enter="3">{lede}</p>' if lede else ""
    act_html = f'<div class="hero__actions" data-enter="4">{actions}</div>' if actions else ""
    return f'''<section class="hero{" hero--tall" if tall else ""}{(" " + extra) if extra else ""}">
<div class="hero__bg" aria-hidden="true">{c["photo"](photo_key, alt, eager=True)}</div>
<div class="container container--wide">
<div class="hero__inner">
{crumb_html}
<span class="eyebrow" data-enter="1">{tag}</span>
<h1 data-enter="2">{title}</h1>
{lede_html}
{act_html}
</div>
</div>
<div class="hero__diag" aria-hidden="true"></div>
</section>
'''


def practice_strip(c):
    r = c["root"]
    items = "".join(f'<li><a href="{r}services/{sl}.html">{SERVICES[sl]["name"]}</a></li>' for sl in c["SERVICE_ORDER"])
    return f'<div class="strip"><span class="strip__label">Practices</span><ul role="list">{items}</ul></div>'


def office_links(c, sep=" &middot; "):
    return sep.join(f'<a href="{maps}">{city.split(",")[0]}</a>' for role, city, addr, maps in c["OFFICES"][1:])


def tile(c, icon_name, title, body="", href=None, extra="", link_text="Learn more"):
    I = c["icon"]
    tag = "a" if href else "div"
    h = f' href="{href}"' if href else ""
    link = f'<span class="link-arrow">{link_text} {I("arrow-right")}</span>' if href else ""
    bodyp = f"<p>{body}</p>" if body else ""
    return f'<{tag} class="tile {extra}"{h}><span class="tile__icon">{I(icon_name)}</span><h3>{title}</h3>{bodyp}{link}</{tag}>'


def _service_tile(c, slug, extra=""):
    s = SERVICES[slug]
    return tile(c, s["icon"], s["name"], s["tag"] + ".", f'{c["root"]}services/{slug}.html', extra, "Explore service")


def numbered_list(items, cls="numlist"):
    lis = "".join(f'<li><span class="numlist__n">0{k}</span><div><h3>{t}</h3><p>{b}</p></div></li>' for k, (t, b) in enumerate(items, 1))
    return f'<ol class="{cls}" role="list">{lis}</ol>'


def columns(items, cls="cols"):
    lis = "".join(f'<li><h3>{t}</h3><p>{b}</p></li>' for t, b in items)
    return f'<ul class="{cls}" role="list">{lis}</ul>'


def contact_section(c, heading="Start a conversation", lede="Tell us about the landscape and the question you are trying to answer. A consultant from the relevant practice replies within one working day."):
    r, I = c["root"], c["icon"]
    topics = ["SAP S/4HANA or migration", "SAP application development or Fiori", "Application management and support", "Supply-chain planning (IBP, PP/DS)", "Serialization (Advanced Track &amp; Trace)", "ComplianceWire", "HR systems (SuccessFactors, Workday)", "SAP AI", "Something else"]
    topic_opts = "".join(f'<option value="{t.replace("&amp;", "&")}">{t}</option>' for t in topics)
    return f'''<section class="section section--rule" id="contact" aria-labelledby="conv-h">
<div class="container container--wide convo">
<div class="convo__details">
<span class="eyebrow">Contact</span>
<h2 id="conv-h">{heading}</h2>
<p class="lede">{lede}</p>
<dl class="convo__dl">
<div><dt>Phone (US)</dt><dd><a href="{c["PHONE_HREF"]}">{c["PHONE_DISPLAY"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{c["EMAIL"]}">{c["EMAIL"]}</a></dd></div>
<div><dt>Head office</dt><dd><a href="{c["OFFICES"][0][3]}">8 Campus Dr, Suite 105, Parsippany, NJ 07054, United States</a></dd></div>
<div><dt>India</dt><dd>{office_links(c)}</dd></div>
</dl>
</div>
<div class="convo__form">
<form class="form" data-form action="mailto:{c["EMAIL"]}" method="post" enctype="text/plain">
<div class="hp-field" aria-hidden="true"><label for="website">Leave this field empty</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
<div class="form__row">
<div class="field"><label for="f-name">Name</label><input type="text" id="f-name" name="name" data-label="Name" required autocomplete="name"><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-company">Company</label><input type="text" id="f-company" name="company" data-label="Company" required autocomplete="organization"><span class="field__error" aria-live="polite"></span></div>
</div>
<div class="form__row">
<div class="field"><label for="f-email">Work email</label><input type="email" id="f-email" name="email" data-label="Email" required autocomplete="email"><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-phone">Phone <span class="optional">(optional)</span></label><input type="tel" id="f-phone" name="phone" data-label="Phone" autocomplete="tel"><span class="field__error" aria-live="polite"></span></div>
</div>
<div class="field"><label for="f-topic">What is this about?</label><select id="f-topic" name="topic" data-label="Topic" required><option value="">Select a topic</option>{topic_opts}</select><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-message">Message</label><textarea id="f-message" name="message" data-label="Message" required minlength="20" placeholder="Current systems, what needs to change, and any timeline you are working to."></textarea><span class="field__error" aria-live="polite"></span></div>
<label class="form__consent"><input type="checkbox" name="consent" data-label="Consent" required><span>I agree that VKollab may use these details to respond to my enquiry.</span><span class="field__error" aria-live="polite"></span></label>
<div class="form__status" role="status" aria-live="polite"></div>
<div class="form__actions"><button class="btn btn--primary btn--lg" type="submit"><span class="spinner" aria-hidden="true"></span>Send message {I("arrow-right")}</button></div>
</form>
</div>
</div>
</section>
'''


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

def home(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    order = c["SERVICE_ORDER"]
    items = "".join(
        f'<li><button type="button" class="svc-list__item{" is-active" if k == 0 else ""}" data-svc="{k}" aria-controls="svc-panel" aria-pressed="{"true" if k == 0 else "false"}"><span class="svc-list__icon">{I(SERVICES[sl]["icon"])}</span>{SERVICES[sl]["name"]}{I("arrow-right")}</button></li>'
        for k, sl in enumerate(order)
    )
    panels = "".join(
        f'''<div class="svc-panel__item{" is-active" if k == 0 else ""}" data-svc-panel="{k}">
<div class="media">{P(SERVICES[sl]["diagram"], SERVICES[sl]["name"])}</div>
<div class="svc-panel__body"><h3>{SERVICES[sl]["name"]}</h3><p>{SERVICES[sl]["description"]}</p><a class="btn btn--white" href="{r}services/{sl}.html">About this service {I("arrow-right")}</a></div>
</div>''' for k, sl in enumerate(order)
    )
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{ind["slug"]}" aria-controls="panel-{ind["slug"]}" aria-selected="{"true" if k == 0 else "false"}" tabindex="{0 if k == 0 else -1}" class="tabs__tab">{ind["name"].replace("Infrastructure Construction", "Construction")}</button>'
        for k, ind in enumerate(INDUSTRIES)
    )
    tab_panels = ""
    for k, ind in enumerate(INDUSTRIES):
        focus = "".join(f'<li>{I("check")}<span>{f}</span></li>' for f in ind["focus"][:3])
        tab_panels += f'''<div role="tabpanel" id="panel-{ind["slug"]}" aria-labelledby="tab-{ind["slug"]}" class="tabs__panel{" is-active" if k == 0 else ""}"{"" if k == 0 else " hidden"}>
<div class="tabs__text"><h3>{ind["name"]}</h3><p>{ind["lede"]}</p><ul class="checklist" role="list">{focus}</ul><a class="link-arrow" href="{r}industries.html#{ind["slug"]}">How we work in {ind["name"].split(" &")[0].lower() if ind["slug"] != "pharma" else "pharma and life sciences"} {I("arrow-right")}</a></div>
<div class="tabs__media"><div class="media media--photo">{P(ind["slug"], ind["name"])}</div></div>
</div>'''
    steps = "".join(
        f'<li><span class="numlist__n">0{k}</span><h3>{t}</h3><p>{d}</p></li>' for k, (t, d) in enumerate(WORK_STEPS, 1)
    )
    why = numbered_list(WHY)

    return f'''<section class="hero hero--home">
<div class="hero__bg" aria-hidden="true">{P("home", "", eager=True)}</div>
<div class="container container--wide">
<div class="hero__inner">
<span class="eyebrow" data-enter="1">SAP consulting &amp; managed services</span>
<h1 data-enter="2">SAP delivered properly, for manufacturers and regulated industries</h1>
<p class="lede lede--lg" data-enter="3">VKollab implements, migrates and runs SAP for companies in the United States, Europe and Japan: S/4HANA, supply-chain planning, serialization and HR platforms, delivered from New Jersey and three centres in India.</p>
<div class="hero__actions" data-enter="4"><a class="btn btn--primary btn--lg" href="{r}contact.html">Talk to a consultant {I("arrow-right")}</a><a class="btn btn--white btn--lg" href="#services">What we do</a></div>
</div>
</div>
<div class="hero__diag" aria-hidden="true"></div>
</section>

<section class="section" aria-labelledby="who-h">
<div class="container container--wide split split--text-first">
<div>
<span class="eyebrow">Who we are</span>
<h2 id="who-h">An SAP partner that stays after go-live</h2>
<p class="lede">VKollab Technologies was founded in 2020 in Parsippany, New Jersey, around a simple model: smaller, more senior teams; the same people from scoping to support; and long client relationships built by working as an extension of the client's own team.</p>
<p>Today more than ninety consultants and developers work from Hyderabad, Guntur and Vijayawada for clients in the United States, Europe and Japan. The work spans the SAP core (S/4HANA, development, Fiori, migration and application management), supply-chain planning (IBP and PP/DS), serialization and compliance for regulated manufacturers (Advanced Track &amp; Trace, ComplianceWire), HR platforms (SuccessFactors, Workday) and, increasingly, AI inside SAP processes.</p>
<a class="link-arrow" href="{r}about.html">About VKollab {I("arrow-right")}</a>
</div>
<div class="media media--photo media--tall" data-reveal>{P("about-trio", "VKollab consultants reviewing a solution design")}</div>
</div>
</section>

<section class="section section--sky" id="services" aria-labelledby="svc-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">What we do</span><h2 id="svc-h">Ten services, one accountable team</h2><p class="lede">From a landscape assessment to a managed service, the same practice owns the work. Select a service to see what it covers.</p></div>
<div class="svc" data-reveal>
<ul class="svc-list" role="list">{items}</ul>
<div class="svc-panel" id="svc-panel">{panels}</div>
</div>
</div>
</section>

<section class="section" aria-labelledby="why-h">
<div class="container container--wide split split--wide">
<div class="split__sticky">
<span class="eyebrow">Why VKollab</span>
<h2 id="why-h">What is different about working with us</h2>
<p class="lede">Four commitments that shape every engagement.</p>
<a class="btn btn--outline" href="{r}contact.html">Ask us about your programme</a>
</div>
{why}
</div>
</section>

<section class="section section--rule" aria-labelledby="ind-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">Who we serve</span><h2 id="ind-h">Industries we serve</h2><p class="lede">Pharmaceutical and life-sciences clients account for two of our practices; the rest of the work is in discrete and process manufacturing and the service industries around them.</p></div>
<div class="tabs" data-tabs>
<div class="tabs__list" role="tablist" aria-label="Industries">{tabs}</div>
{tab_panels}
</div>
</div>
</section>

<section class="section section--navy" aria-labelledby="proc-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">How we work</span><h2 id="proc-h">The same four stages on every programme</h2></div>
<ol class="steps4" role="list" data-reveal-stagger>{steps}</ol>
</div>
</section>

{contact_section(c)}
'''


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def about(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    values = columns(VALUES, "cols cols--4")
    offices = "".join(
        f'<li><strong>{city}</strong><span>{role}</span><address>{addr}</address><a class="link-arrow" href="{maps}">Map {I("external")}</a></li>'
        for role, city, addr, maps in c["OFFICES"]
    )
    mvv = columns([
        ("Mission", "To deliver measurable business outcomes for our clients by implementing and running SAP well, and to be the team they call first when the next programme starts."),
        ("Vision", "To be the SAP partner of choice for mid-sized manufacturers and regulated companies in the United States, Europe and Japan: senior enough to be trusted with the core, small enough to know every client by name."),
        ("How we deliver", "Senior consultants on every engagement, scope and risk stated plainly, the same team from assessment to support, and clean-core discipline so each upgrade stays a standard upgrade."),
    ], "cols cols--3")
    return hero(
        c, "about-hero", "About VKollab", "Who we are",
        "An SAP consulting and managed-services firm, founded in 2020, with a head office in New Jersey and more than ninety consultants in India.",
        "", crumbs=[("Home", r + "index.html"), ("About", None)], alt="VKollab team",
    ) + f'''

<section class="section" aria-labelledby="story-h">
<div class="container container--wide split split--text-first">
<div>
<span class="eyebrow">Our story</span>
<h2 id="story-h">Built to do SAP work properly, and to stay for the run</h2>
<p class="lede">VKollab Technologies was incorporated in February 2020 in Parsippany, New Jersey. The model it was built on is deliberately simple: the people who sell an SAP programme are the people who deliver it, and they do not leave at go-live.</p>
<p>Engagements are led by consultants who have delivered the same scope before. The team that scopes a programme builds it, takes it live and then supports it under an SLA. Delivery centres in Hyderabad, Guntur and Vijayawada give clients a team that works their hours and the overnight windows between them.</p>
<p>Two practices grew directly out of client demand in pharmaceutical and life sciences: SAP Advanced Track &amp; Trace for serialization and regulatory reporting, and ComplianceWire for validated training. They sit alongside the SAP core, supply-chain planning, HR platforms and AI work that make up the rest of the portfolio.</p>
</div>
<div class="media media--photo media--tall" data-reveal>{P("about-board", "VKollab consultants in a planning session")}</div>
</div>
</section>

<section class="section section--sky" aria-labelledby="lead-h">
<div class="container container--wide split">
<div>
<span class="eyebrow">Leadership</span>
<h2 id="lead-h">Led by people who still do the work</h2>
<p class="lede">VKollab is founder-led. The leadership team reviews every proposal and stays involved through delivery; there is no separate sales organisation.</p>
</div>
<div class="leader" data-reveal>
<img src="{r}assets/images/ceo-venkat-makke.jpg" alt="Venkat Makke" width="400" height="400" loading="lazy">
<div>
<h3>Venkat Makke</h3>
<p class="leader__role">Founder &amp; Chief Executive Officer</p>
<p>Venkat founded VKollab in 2020 and leads the firm from the Parsippany head office. He remains accountable for every client relationship.</p>
<a class="link-arrow" href="https://www.linkedin.com/in/venkatmakke/">LinkedIn {I("external")}</a>
</div>
</div>
</div>
</section>

<section class="section" aria-labelledby="mvv-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">Mission, vision and method</span><h2 id="mvv-h">What we are here to do</h2></div>
{mvv}
</div>
</section>

<section class="section section--rule" aria-labelledby="val-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">Values</span><h2 id="val-h">How we behave when it matters</h2></div>
{values}
</div>
</section>

<section class="section section--sky" id="offices" aria-labelledby="off-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">Where we are</span><h2 id="off-h">Four offices, two time zones</h2></div>
<ul class="offices" role="list" data-reveal-stagger>{offices}</ul>
</div>
</section>

{c["cta_band"](r)}
'''


# ---------------------------------------------------------------------------
# SERVICES HUB
# ---------------------------------------------------------------------------

def services_hub(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    tiles_html = "".join(_service_tile(c, sl) for sl in c["SERVICE_ORDER"])
    eng = columns(ENGAGEMENTS, "cols cols--4")
    return hero(
        c, "office", "Services", "What we do",
        "Ten services covering the SAP core, user experience, migration, planning, serialization and compliance, HR platforms and AI. Each is run by consultants who have delivered it before.",
        f'<a class="btn btn--primary btn--lg" href="{r}contact.html">Talk to a consultant {I("arrow-right")}</a>',
        crumbs=[("Home", r + "index.html"), ("Services", None)], alt="VKollab consultants",
    ) + f'''
<section class="section" id="services" aria-labelledby="all-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">All services</span><h2 id="all-h">Choose the service closest to your question</h2><p class="lede">Most programmes combine two or three of these. If you are not sure where to start, a landscape assessment is the usual first step.</p></div>
<div class="tiles" data-reveal-stagger>{tiles_html}</div>
</div>
</section>

<section class="section section--sky" aria-labelledby="eng-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">How we engage</span><h2 id="eng-h">Project, managed service, extended team or advisory</h2></div>
{eng}
</div>
</section>

{c["cta_band"](r)}
'''


# ---------------------------------------------------------------------------
# SERVICE DETAIL
# ---------------------------------------------------------------------------

def service_page(c, slug, practice=None):
    r, I, P = c["root"], c["icon"], c["photo"]
    s = SERVICES[slug]
    aside_links = "".join(
        f'<a href="{r}services/{x}.html"{" aria-current=\"page\"" if x == slug else ""}>{SERVICES[x]["name"]}{I("arrow-right")}</a>'
        for x in c["SERVICE_ORDER"]
    )
    cap = "".join(f'<li><h3>{t}</h3><p>{b}</p></li>' for t, b in s["capability"])
    appr = "".join(f'<li><span class="numlist__n">0{k}</span><div><h3>{t}</h3><p>{b}</p></div></li>' for k, (t, b) in enumerate(s["approach"], 1))
    deliv = "".join(f'<li>{I("check")}<span>{d}</span></li>' for d in s["deliverables"])
    outc = "".join(f'<li><h3>{t}</h3><p>{b}</p></li>' for t, b in s["outcomes"])
    uses = "".join(f'<li>{I("check")}<span>{u}</span></li>' for u in s["use_cases"])
    related = "".join(_service_tile(c, x) for x in s["related"])
    industries_for = [ind for ind in INDUSTRIES if slug in ind["services"]]
    ind_links = ", ".join(f'<a href="{r}industries.html#{ind["slug"]}">{ind["name"]}</a>' for ind in industries_for) or "all sectors we serve"

    return hero(
        c, s["diagram"], "Services", s["name"], s["intro"],
        f'<a class="btn btn--primary btn--lg" href="{r}contact.html">Talk to a consultant {I("arrow-right")}</a><a class="btn btn--white btn--lg" href="#approach">How we deliver it</a>',
        crumbs=[("Home", r + "index.html"), ("Services", r + "services.html"), (s["name"], None)], alt=s["name"],
    ) + f'''
<div class="container container--wide section">
<div class="service-layout">
<div class="service-body">

<section aria-labelledby="prob-h">
<span class="eyebrow">The challenge</span>
<h2 id="prob-h">Why organisations come to us for this</h2>
<div class="callout"><p>{s["problem"]}</p></div>
</section>

<section aria-labelledby="cap-h">
<span class="eyebrow">Capabilities</span>
<h2 id="cap-h">What the service covers</h2>
<ul class="cols cols--2 cols--tight" role="list" data-reveal-stagger>{cap}</ul>
</section>

<section id="approach" aria-labelledby="appr-h">
<span class="eyebrow">Our approach</span>
<h2 id="appr-h">How we deliver it</h2>
<ol class="numlist" role="list" data-reveal-stagger>{appr}</ol>
</section>

<section aria-labelledby="out-h" class="service-outcomes">
<span class="eyebrow">What changes</span>
<h2 id="out-h">Outcomes clients can measure</h2>
<ul class="cols cols--2 cols--tight" role="list" data-reveal-stagger>{outc}</ul>
</section>

<section aria-labelledby="del-h">
<span class="eyebrow">In practice</span>
<h2 id="del-h">What you receive, and where it is used</h2>
<div class="two-col" data-reveal>
<div><h3>Deliverables</h3><ul class="checklist" role="list">{deliv}</ul></div>
<div><h3>Typical situations</h3><ul class="checklist" role="list">{uses}</ul><p class="meta" style="margin-top:1.25rem">Relevant industries: {ind_links}.</p></div>
</div>
</section>

<div class="related">
<span class="eyebrow">Related services</span>
<div class="tiles tiles--3" data-reveal-stagger>{related}</div>
</div>

</div>

<aside aria-label="Service navigation">
<div class="sticky">
<div class="aside-card"><h2>All services</h2><nav>{aside_links}</nav></div>
<div class="aside-card aside-card--cta">
<h3>Discuss {s["name"]}</h3>
<p>Send a short description of your landscape and the question you are trying to answer. A consultant from this practice will reply within one working day.</p>
<a class="btn btn--primary" href="{r}contact.html">Talk to a consultant {I("arrow-right")}</a>
<p style="margin-top:1rem"><a href="{c["PHONE_HREF"]}">{c["PHONE_DISPLAY"]}</a></p>
</div>
</div>
</aside>
</div>
</div>

{c["cta_band"](r, heading=f"Talk to us about {s['name']}")}
'''


# ---------------------------------------------------------------------------
# INDUSTRIES
# ---------------------------------------------------------------------------

def industries(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    index = "".join(f'<a href="#{ind["slug"]}">{ind["name"]}</a>' for ind in INDUSTRIES)
    blocks = ""
    for k, ind in enumerate(INDUSTRIES):
        focus = "".join(f'<li>{I("check")}<span>{f}</span></li>' for f in ind["focus"])
        svcs = "".join(f'<a href="{r}services/{s}.html">{SERVICES[s]["name"]}</a>' for s in ind["services"])
        blocks += f'''<article class="industry-block" id="{ind["slug"]}">
<div class="industry-block__media" data-reveal><div class="media media--photo">{P(ind["slug"], ind["name"])}</div></div>
<div class="industry-block__body">
<span class="eyebrow">0{k + 1} &mdash; Industry</span>
<h2>{ind["name"]}</h2>
<p class="lede">{ind["lede"]}</p>
<p>{ind["body"]}</p>
<h3>Where we focus</h3>
<ul class="checklist" role="list">{focus}</ul>
<h3>Relevant services</h3>
<div class="cluster cluster--links">{svcs}</div>
</div>
</article>'''
    return hero(
        c, "industry-tech", "Industries", "Who we serve",
        "Pharmaceutical and life-sciences clients account for two of our practices. The rest of our work is in discrete and process manufacturing and the service industries around them.",
        f'<nav aria-label="Industries on this page" class="industries-index">{index}</nav>',
        crumbs=[("Home", r + "index.html"), ("Industries", None)], alt="Manufacturing operations",
    ) + f'''
<section class="section" style="padding-top:1rem"><div class="container container--wide">{blocks}</div></section>
{c["cta_band"](r, heading="Working in a sector we have not listed?", body="Most of what we do transfers between industries: the SAP core, planning and HR platforms are the same. Tell us about the business and we will say honestly whether we are the right fit.")}
'''


# ---------------------------------------------------------------------------
# CAREERS
# ---------------------------------------------------------------------------

def careers(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    work = columns([
        ("S/4HANA and the SAP core", "Conversions, new implementations, custom development, Fiori and application management for US and European clients."),
        ("Planning and serialization", "SAP IBP, embedded PP/DS, Advanced Track &amp; Trace and ComplianceWire, mostly for pharmaceutical and manufacturing clients."),
        ("HR platforms and AI", "SuccessFactors and Workday implementations, and AI use cases inside SAP finance, procurement and supply-chain processes."),
    ], "cols cols--3")
    return hero(
        c, "careers", "Careers", "Work on SAP programmes that go live",
        "VKollab hires experienced SAP consultants and developers in Hyderabad, Guntur and Vijayawada, and occasionally in New Jersey. We are an equal-opportunity employer.",
        f'<a class="btn btn--primary btn--lg" href="#apply">Send your CV {I("arrow-right")}</a>',
        crumbs=[("Home", r + "index.html"), ("Careers", None)], alt="VKollab consultant at her desk",
    ) + f'''
<section class="section" aria-labelledby="why-h">
<div class="container container--wide split split--text-first">
<div>
<span class="eyebrow">Why VKollab</span>
<h2 id="why-h">Senior work, a team that knows your name</h2>
<p class="lede">With around ninety people we are large enough to run full S/4HANA programmes and small enough that leadership knows every consultant. You work directly with clients, not through layers of account management.</p>
<ul class="checklist" role="list">
<li>{I("check")}<span>Client-facing work from the first assignment, with a senior consultant alongside you</span></li>
<li>{I("check")}<span>Structured training on current SAP releases; technology moves quickly and we keep people current</span></li>
<li>{I("check")}<span>Offices in Ameerpet (Hyderabad), Guntur and Vijayawada; hybrid working by agreement with your practice lead</span></li>
<li>{I("check")}<span>Programmes for clients in the United States, Europe and Japan, with travel where the work needs it</span></li>
</ul>
</div>
<div class="media media--photo media--tall" data-reveal>{P("team2", "VKollab team in a working session")}</div>
</div>
</section>

<section class="section section--sky" aria-labelledby="work-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">What you will work on</span><h2 id="work-h">Three areas, all of them live client work</h2></div>
{work}
</div>
</section>

<section class="section section--navy" id="apply" aria-labelledby="apply-h">
<div class="container container--wide reach">
<div>
<span class="eyebrow">Apply</span>
<h2 id="apply-h">Send your CV</h2>
<p class="lede">We are always interested in SAP functional and technical consultants, developers, planning specialists and serialization experts. Put the role or module in the subject line.</p>
</div>
<div class="reach__action">
<a class="reach__mail" href="mailto:{c["CAREERS_EMAIL"]}?subject=Application">{I("mail")}<span>{c["CAREERS_EMAIL"]}</span></a>
<div class="cluster"><a class="btn btn--primary btn--lg" href="mailto:{c["CAREERS_EMAIL"]}?subject=Application">Email your CV {I("arrow-right")}</a><a class="btn btn--white btn--lg" href="{r}contact.html">Other enquiries</a></div>
</div>
</div>
</section>
'''


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

def contact(c):
    r, I = c["root"], c["icon"]
    offices = "".join(
        f'<li><strong>{city}</strong><span>{role}</span><address>{addr}</address><a class="link-arrow" href="{maps}">Map {I("external")}</a></li>'
        for role, city, addr, maps in c["OFFICES"]
    )
    topics = ["SAP S/4HANA or migration", "SAP application development or Fiori", "Application management and support", "Supply-chain planning (IBP, PP/DS)", "Serialization (Advanced Track & Trace)", "ComplianceWire", "HR systems (SuccessFactors, Workday)", "SAP AI", "Careers", "Something else"]
    topic_opts = "".join(f'<option value="{t}">{t}</option>' for t in topics)
    return hero(
        c, "contact", "Contact", "Talk to a consultant",
        "Describe the landscape and the question you are trying to answer. A consultant from the relevant practice replies within one working day.",
        "", crumbs=[("Home", r + "index.html"), ("Contact", None)], alt="VKollab consultant",
    ) + f'''
<section class="section">
<div class="container container--wide contact-layout">
<div class="contact-channels" data-reveal-stagger>
<dl class="convo__dl">
<div><dt>Phone (US head office)</dt><dd><a href="{c["PHONE_HREF"]}">{c["PHONE_DISPLAY"]}</a><small>Coverage across US and Indian business hours</small></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{c["EMAIL"]}">{c["EMAIL"]}</a><small>Enquiries, proposals and partnerships. For roles, see <a href="{r}careers.html">Careers</a>.</small></dd></div>
<div><dt>Head office</dt><dd>8 Campus Dr, Suite 105<br>Parsippany, NJ 07054, United States<small><a href="{c["OFFICES"][0][3]}">Open in Maps</a></small></dd></div>
</dl>
</div>

<div class="contact-form-wrap">
<h2>Send a message</h2>
<p>Share enough context for us to route you to the right person. A few sentences will do.</p>
<form class="form" data-form action="mailto:{c["EMAIL"]}" method="post" enctype="text/plain">
<div class="hp-field" aria-hidden="true"><label for="website">Leave this field empty</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
<div class="form__row">
<div class="field"><label for="f-name">Name</label><input type="text" id="f-name" name="name" data-label="Name" required autocomplete="name"><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-company">Company</label><input type="text" id="f-company" name="company" data-label="Company" required autocomplete="organization"><span class="field__error" aria-live="polite"></span></div>
</div>
<div class="form__row">
<div class="field"><label for="f-email">Work email</label><input type="email" id="f-email" name="email" data-label="Email" required autocomplete="email"><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-phone">Phone <span class="optional">(optional)</span></label><input type="tel" id="f-phone" name="phone" data-label="Phone" autocomplete="tel"><span class="field__error" aria-live="polite"></span></div>
</div>
<div class="field"><label for="f-topic">What is this about?</label><select id="f-topic" name="topic" data-label="Topic" required><option value="">Select a topic</option>{topic_opts}</select><span class="field__error" aria-live="polite"></span></div>
<div class="field"><label for="f-message">Message</label><textarea id="f-message" name="message" data-label="Message" required minlength="20" placeholder="Current systems, what needs to change, and any timeline you are working to."></textarea><span class="field__error" aria-live="polite"></span><span class="field__hint">Please do not include passwords or confidential data.</span></div>
<label class="form__consent"><input type="checkbox" name="consent" data-label="Consent" required><span>I agree that VKollab may use these details to respond to my enquiry.</span><span class="field__error" aria-live="polite"></span></label>
<div class="form__status" role="status" aria-live="polite"></div>
<div class="form__actions"><button class="btn btn--primary btn--lg" type="submit"><span class="spinner" aria-hidden="true"></span>Send message {I("arrow-right")}</button><span class="meta">Or call <a href="{c["PHONE_HREF"]}">{c["PHONE_DISPLAY"]}</a></span></div>
</form>
</div>
</div>
</section>

<section class="section section--sky" id="offices" aria-labelledby="off-h">
<div class="container container--wide">
<div class="section-head section-head--left"><span class="eyebrow">Our offices</span><h2 id="off-h">Where to find us</h2></div>
<ul class="offices" role="list" data-reveal-stagger>{offices}</ul>
</div>
</section>
'''


# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

def not_found(c):
    r, I, P = c["root"], c["icon"], c["photo"]
    links = [("index.html", "Home"), ("services.html", "Services"), ("industries.html", "Industries"), ("about.html", "About"), ("careers.html", "Careers"), ("contact.html", "Contact")]
    lis = "".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in links)
    return f'''
<section class="error-page">
<div class="hero__bg" aria-hidden="true">{P("office", "", eager=True)}</div>
<div class="container error-page__inner">
<span class="eyebrow">Error 404</span>
<p class="display" aria-hidden="true">404</p>
<h1>Page not found</h1>
<p class="lede">The page may have moved when the site was rebuilt, or the address was typed incorrectly.</p>
<div class="cluster cluster--center"><a class="btn btn--primary btn--lg" href="{r}index.html">Back to the homepage {I("arrow-right")}</a><a class="btn btn--white btn--lg" href="{r}contact.html">Contact us</a></div>
<ul class="error-links" role="list">{lis}</ul>
</div>
</section>
'''


# ---------------------------------------------------------------------------
# LEGAL
# ---------------------------------------------------------------------------

def _legal(c, crumb, title, intro, sections):
    r = c["root"]
    body = "".join(f"<h2>{h}</h2>{p}" for h, p in sections)
    return hero(c, "hero", "Legal", title, "", "", crumbs=[("Home", r + "index.html"), (crumb, None)], alt="VKollab office") + f'''
<section class="section" aria-label="{title}">
<div class="container legal">
<p class="meta">Last updated: September 2026</p>
<p class="lede">{intro}</p>
{body}
<p>Questions about this page can be sent to <a href="mailto:{c["EMAIL"]}">{c["EMAIL"]}</a>.</p>
</div>
</section>
'''


def privacy(c):
    return _legal(c, "Privacy Policy", "Privacy Policy",
        "VKollab Technologies (\"VKollab\", \"we\", \"us\") respects your privacy. This policy explains what information we collect through vkollab.com, how we use it, and the choices you have.",
        [
            ("Information we collect", "<p>We collect the information you choose to give us when you use the contact form, write to us by email or apply for a role: your name, company, email address, phone number, the subject of your enquiry, your message, and any CV or documents you attach. Our web server may also record standard technical data such as your IP address, browser type and the pages requested, which is used only to keep the site secure and running.</p>"),
            ("How we use it", "<p>We use the information you provide to respond to your enquiry, to evaluate your application, to deliver and improve our services and to meet our legal obligations. We do not sell personal information and we do not use it for automated decision-making.</p>"),
            ("Cookies and analytics", "<p>This website does not set tracking cookies and does not load third-party advertising or analytics scripts. Links to external sites and services (for example Google Maps, LinkedIn, the VKONNECT alumni portal and the HR App) are governed by those providers' own privacy policies.</p>"),
            ("Sharing", "<p>Your information is shared only with VKollab staff who need it to handle your request, with service providers who process it on our behalf under confidentiality obligations (for example email hosting), and where required by law.</p>"),
            ("Retention and security", "<p>Enquiries are retained for as long as needed to deal with them and for a reasonable period afterwards. Applications are retained for the duration of the recruitment process unless you ask us to keep your CV on file. We use appropriate technical and organisational measures to protect your information.</p>"),
            ("Your rights", "<p>Depending on where you live, you may have the right to access, correct or delete the personal information we hold about you, to object to or restrict its processing, and to lodge a complaint with a supervisory authority. To exercise any of these rights, email us at the address below.</p>"),
            ("Changes", "<p>We may update this policy from time to time. The date at the top shows when it was last revised.</p>"),
        ])


def terms(c):
    return _legal(c, "Terms and Conditions", "Terms and Conditions",
        "By accessing vkollab.com you agree to the following terms. If you do not agree with them, please do not use this website.",
        [
            ("Use of the website", "<p>This website is provided for general information about VKollab Technologies and its services. You may browse, print and download material for your own non-commercial reference, provided you keep all copyright and proprietary notices intact. You may not use the site in any way that is unlawful, that could damage or impair it, or that interferes with anyone else's use of it.</p>"),
            ("Intellectual property", "<p>Unless stated otherwise, the content of this website — text, graphics, logos, photographs and page design — is owned by or licensed to VKollab Technologies and is protected by copyright and trademark law. SAP, SAP S/4HANA, SAP Fiori, SAP IBP, SAP SuccessFactors and other SAP products are trademarks of SAP SE. Workday is a trademark of Workday, Inc. ComplianceWire is a trademark of UL. All other marks belong to their respective owners.</p>"),
            ("No professional advice", "<p>Information on this site is provided in good faith for general guidance only and does not constitute professional, legal or contractual advice. Any engagement with VKollab is governed by a separate written agreement.</p>"),
            ("Disclaimer and limitation of liability", "<p>The website is provided \"as is\" without warranties of any kind. To the fullest extent permitted by law, VKollab Technologies accepts no liability for any loss or damage arising from the use of, or reliance on, this website or any site linked from it.</p>"),
            ("External links", "<p>Links to third-party websites and services are provided for convenience. VKollab does not control and is not responsible for their content or practices.</p>"),
            ("Governing law", "<p>These terms are governed by the laws of the State of New Jersey, United States, and any dispute arising from them will be subject to the exclusive jurisdiction of the courts located there.</p>"),
            ("Changes", "<p>We may revise these terms at any time by updating this page. Continued use of the website after a change constitutes acceptance of the revised terms.</p>"),
        ])
