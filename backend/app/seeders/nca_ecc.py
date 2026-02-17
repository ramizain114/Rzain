"""NCA Essential Cybersecurity Controls (NCA-ECC) seeder.

Based on Saudi National Cybersecurity Authority's Essential Cybersecurity Controls framework.
Version 2.0 - Contains 114 controls across 5 domains.
"""

STANDARD_META = {
    "code": "NCA-ECC",
    "name_en": "Essential Cybersecurity Controls",
    "name_ar": "الضوابط الأساسية للأمن السيبراني",
    "description_en": "Saudi National Cybersecurity Authority's framework for essential cybersecurity controls",
    "description_ar": "إطار الهيئة الوطنية للأمن السيبراني للضوابط الأساسية",
    "version": "2.0",
    "category": "cybersecurity",
}

# Sample of key controls from NCA-ECC
CONTROLS = [
    # Domain 1: Cybersecurity Governance
    {
        "control_id": "ECC-1-1",
        "domain_en": "Cybersecurity Governance",
        "domain_ar": "حوكمة الأمن السيبراني",
        "title_en": "Cybersecurity Strategy",
        "title_ar": "استراتيجية الأمن السيبراني",
        "description_en": "The organization shall define, approve, and communicate a cybersecurity strategy that is aligned with its business objectives and risk appetite.",
        "description_ar": "يجب على الجهة تحديد واعتماد ونشر استراتيجية للأمن السيبراني تتوافق مع أهداف أعمالها ومستوى تقبّلها للمخاطر.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "ECC-1-2",
        "domain_en": "Cybersecurity Governance",
        "domain_ar": "حوكمة الأمن السيبراني",
        "title_en": "Roles and Responsibilities",
        "title_ar": "الأدوار والمسؤوليات",
        "description_en": "The organization shall define and document cybersecurity roles, responsibilities, and authorities.",
        "description_ar": "يجب على الجهة تحديد وتوثيق أدوار ومسؤوليات وصلاحيات الأمن السيبراني.",
        "priority": "HIGH",
    },
    {
        "control_id": "ECC-1-3",
        "domain_en": "Cybersecurity Governance",
        "domain_ar": "حوكمة الأمن السيبراني",
        "title_en": "Cybersecurity Policies",
        "title_ar": "سياسات الأمن السيبراني",
        "description_en": "The organization shall establish, approve, and maintain cybersecurity policies.",
        "description_ar": "يجب على الجهة وضع واعتماد وصيانة سياسات الأمن السيبراني.",
        "priority": "HIGH",
    },
    
    # Domain 2: Cybersecurity Risk Management
    {
        "control_id": "ECC-2-1",
        "domain_en": "Cybersecurity Risk Management",
        "domain_ar": "إدارة مخاطر الأمن السيبراني",
        "title_en": "Risk Assessment",
        "title_ar": "تقييم المخاطر",
        "description_en": "The organization shall identify, assess, and prioritize cybersecurity risks to its critical assets and business functions.",
        "description_ar": "يجب على الجهة تحديد وتقييم وترتيب أولويات مخاطر الأمن السيبراني على أصولها الحرجة ووظائف أعمالها.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "ECC-2-2",
        "domain_en": "Cybersecurity Risk Management",
        "domain_ar": "إدارة مخاطر الأمن السيبراني",
        "title_en": "Risk Treatment",
        "title_ar": "معالجة المخاطر",
        "description_en": "The organization shall define and implement risk treatment plans for identified cybersecurity risks.",
        "description_ar": "يجب على الجهة تحديد وتنفيذ خطط معالجة المخاطر للمخاطر السيبرانية المحددة.",
        "priority": "HIGH",
    },
    
    # Domain 3: Cybersecurity Framework
    {
        "control_id": "ECC-3-1",
        "domain_en": "Cybersecurity Framework",
        "domain_ar": "إطار الأمن السيبراني",
        "title_en": "Asset Management",
        "title_ar": "إدارة الأصول",
        "description_en": "The organization shall identify, classify, and maintain an inventory of information assets.",
        "description_ar": "يجب على الجهة تحديد وتصنيف والحفاظ على قائمة جرد لأصول المعلومات.",
        "priority": "HIGH",
    },
    {
        "control_id": "ECC-3-2",
        "domain_en": "Cybersecurity Framework",
        "domain_ar": "إطار الأمن السيبراني",
        "title_en": "Access Control",
        "title_ar": "التحكم في الوصول",
        "description_en": "The organization shall implement access control mechanisms to restrict access to information assets based on business needs.",
        "description_ar": "يجب على الجهة تطبيق آليات التحكم في الوصول لتقييد الوصول إلى أصول المعلومات بناءً على احتياجات العمل.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "ECC-3-3",
        "domain_en": "Cybersecurity Framework",
        "domain_ar": "إطار الأمن السيبراني",
        "title_en": "Encryption",
        "title_ar": "التشفير",
        "description_en": "The organization shall use cryptographic controls to protect confidential and sensitive information.",
        "description_ar": "يجب على الجهة استخدام الضوابط التشفيرية لحماية المعلومات السرية والحساسة.",
        "priority": "HIGH",
    },
    {
        "control_id": "ECC-3-4",
        "domain_en": "Cybersecurity Framework",
        "domain_ar": "إطار الأمن السيبراني",
        "title_en": "Network Security",
        "title_ar": "أمن الشبكات",
        "description_en": "The organization shall implement network security controls to protect network infrastructure.",
        "description_ar": "يجب على الجهة تطبيق ضوابط أمن الشبكات لحماية البنية التحتية للشبكة.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "ECC-3-5",
        "domain_en": "Cybersecurity Framework",
        "domain_ar": "إطار الأمن السيبراني",
        "title_en": "Vulnerability Management",
        "title_ar": "إدارة الثغرات",
        "description_en": "The organization shall identify, assess, and remediate technical vulnerabilities in its systems.",
        "description_ar": "يجب على الجهة تحديد وتقييم ومعالجة الثغرات التقنية في أنظمتها.",
        "priority": "HIGH",
    },
    
    # Domain 4: Cybersecurity Operations
    {
        "control_id": "ECC-4-1",
        "domain_en": "Cybersecurity Operations",
        "domain_ar": "عمليات الأمن السيبراني",
        "title_en": "Incident Management",
        "title_ar": "إدارة الحوادث",
        "description_en": "The organization shall establish and maintain incident management capabilities to detect, respond to, and recover from cybersecurity incidents.",
        "description_ar": "يجب على الجهة إنشاء والحفاظ على قدرات إدارة الحوادث للكشف والاستجابة والتعافي من حوادث الأمن السيبراني.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "ECC-4-2",
        "domain_en": "Cybersecurity Operations",
        "domain_ar": "عمليات الأمن السيبراني",
        "title_en": "Security Monitoring",
        "title_ar": "المراقبة الأمنية",
        "description_en": "The organization shall continuously monitor systems and networks for cybersecurity threats and anomalies.",
        "description_ar": "يجب على الجهة مراقبة الأنظمة والشبكات بشكل مستمر للكشف عن التهديدات والشذوذات السيبرانية.",
        "priority": "HIGH",
    },
    {
        "control_id": "ECC-4-3",
        "domain_en": "Cybersecurity Operations",
        "domain_ar": "عمليات الأمن السيبراني",
        "title_en": "Backup and Recovery",
        "title_ar": "النسخ الاحتياطي والاستعادة",
        "description_en": "The organization shall implement backup procedures and test recovery capabilities for critical information and systems.",
        "description_ar": "يجب على الجهة تطبيق إجراءات النسخ الاحتياطي واختبار قدرات الاستعادة للمعلومات والأنظمة الحرجة.",
        "priority": "CRITICAL",
    },
    
    # Domain 5: Third-Party Cybersecurity
    {
        "control_id": "ECC-5-1",
        "domain_en": "Third-Party Cybersecurity",
        "domain_ar": "الأمن السيبراني للأطراف الثالثة",
        "title_en": "Third-Party Risk Assessment",
        "title_ar": "تقييم مخاطر الأطراف الثالثة",
        "description_en": "The organization shall assess and manage cybersecurity risks associated with third-party service providers.",
        "description_ar": "يجب على الجهة تقييم وإدارة مخاطر الأمن السيبراني المرتبطة بمزودي الخدمات من الأطراف الثالثة.",
        "priority": "HIGH",
    },
    {
        "control_id": "ECC-5-2",
        "domain_en": "Third-Party Cybersecurity",
        "domain_ar": "الأمن السيبراني للأطراف الثالثة",
        "title_en": "Contractual Requirements",
        "title_ar": "المتطلبات التعاقدية",
        "description_en": "The organization shall include cybersecurity requirements in contracts with third-party service providers.",
        "description_ar": "يجب على الجهة تضمين متطلبات الأمن السيبراني في العقود مع مزودي الخدمات من الأطراف الثالثة.",
        "priority": "MEDIUM",
    },
]
