"""NCA Cloud Security Controls (NCA-CSCC) seeder.

Based on Saudi National Cybersecurity Authority's Cloud Security Controls framework.
Contains controls specific to cloud computing environments.
"""

STANDARD_META = {
    "code": "NCA-CSCC",
    "name_en": "Cloud Security Controls",
    "name_ar": "ضوابط أمن الحوسبة السحابية",
    "description_en": "Controls for securing cloud computing environments and services",
    "description_ar": "ضوابط لتأمين بيئات وخدمات الحوسبة السحابية",
    "version": "1.0",
    "category": "cloud_security",
}

CONTROLS = [
    # Cloud Governance
    {
        "control_id": "CSCC-1-1",
        "domain_en": "Cloud Governance",
        "domain_ar": "حوكمة السحابة",
        "title_en": "Cloud Strategy",
        "title_ar": "استراتيجية السحابة",
        "description_en": "The organization shall develop and maintain a cloud adoption strategy aligned with business objectives.",
        "description_ar": "يجب على الجهة تطوير والحفاظ على استراتيجية اعتماد السحابة متوافقة مع أهداف الأعمال.",
        "priority": "HIGH",
    },
    {
        "control_id": "CSCC-1-2",
        "domain_en": "Cloud Governance",
        "domain_ar": "حوكمة السحابة",
        "title_en": "Cloud Service Provider Assessment",
        "title_ar": "تقييم مزود الخدمات السحابية",
        "description_en": "The organization shall assess cloud service providers for compliance with security requirements.",
        "description_ar": "يجب على الجهة تقييم مزودي الخدمات السحابية للامتثال لمتطلبات الأمان.",
        "priority": "CRITICAL",
    },
    
    # Data Security in Cloud
    {
        "control_id": "CSCC-2-1",
        "domain_en": "Data Security",
        "domain_ar": "أمن البيانات",
        "title_en": "Data Classification in Cloud",
        "title_ar": "تصنيف البيانات في السحابة",
        "description_en": "The organization shall classify data before moving it to cloud environments.",
        "description_ar": "يجب على الجهة تصنيف البيانات قبل نقلها إلى بيئات السحابة.",
        "priority": "HIGH",
    },
    {
        "control_id": "CSCC-2-2",
        "domain_en": "Data Security",
        "domain_ar": "أمن البيانات",
        "title_en": "Encryption in Transit and at Rest",
        "title_ar": "التشفير أثناء النقل وفي حالة السكون",
        "description_en": "The organization shall encrypt sensitive data in transit and at rest in cloud environments.",
        "description_ar": "يجب على الجهة تشفير البيانات الحساسة أثناء النقل وفي حالة السكون في بيئات السحابة.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "CSCC-2-3",
        "domain_en": "Data Security",
        "domain_ar": "أمن البيانات",
        "title_en": "Data Residency",
        "title_ar": "إقامة البيانات",
        "description_en": "The organization shall ensure data is stored in compliant geographic locations as per regulatory requirements.",
        "description_ar": "يجب على الجهة التأكد من تخزين البيانات في مواقع جغرافية متوافقة وفقًا للمتطلبات التنظيمية.",
        "priority": "CRITICAL",
    },
    
    # Identity and Access Management
    {
        "control_id": "CSCC-3-1",
        "domain_en": "Identity and Access Management",
        "domain_ar": "إدارة الهوية والوصول",
        "title_en": "Cloud Identity Management",
        "title_ar": "إدارة الهوية السحابية",
        "description_en": "The organization shall implement strong identity and access management for cloud services.",
        "description_ar": "يجب على الجهة تطبيق إدارة قوية للهوية والوصول للخدمات السحابية.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "CSCC-3-2",
        "domain_en": "Identity and Access Management",
        "domain_ar": "إدارة الهوية والوصول",
        "title_en": "Multi-Factor Authentication",
        "title_ar": "المصادقة متعددة العوامل",
        "description_en": "The organization shall enforce multi-factor authentication for cloud service access.",
        "description_ar": "يجب على الجهة فرض المصادقة متعددة العوامل للوصول إلى الخدمات السحابية.",
        "priority": "HIGH",
    },
    
    # Cloud Infrastructure Security
    {
        "control_id": "CSCC-4-1",
        "domain_en": "Infrastructure Security",
        "domain_ar": "أمن البنية التحتية",
        "title_en": "Network Segmentation",
        "title_ar": "تقسيم الشبكة",
        "description_en": "The organization shall implement network segmentation in cloud environments to isolate workloads.",
        "description_ar": "يجب على الجهة تطبيق تقسيم الشبكة في بيئات السحابة لعزل أحمال العمل.",
        "priority": "HIGH",
    },
    {
        "control_id": "CSCC-4-2",
        "domain_en": "Infrastructure Security",
        "domain_ar": "أمن البنية التحتية",
        "title_en": "Security Configuration Management",
        "title_ar": "إدارة التكوين الأمني",
        "description_en": "The organization shall maintain secure configurations for cloud infrastructure and services.",
        "description_ar": "يجب على الجهة الحفاظ على تكوينات آمنة للبنية التحتية والخدمات السحابية.",
        "priority": "HIGH",
    },
    
    # Cloud Security Monitoring
    {
        "control_id": "CSCC-5-1",
        "domain_en": "Security Monitoring",
        "domain_ar": "المراقبة الأمنية",
        "title_en": "Cloud Activity Logging",
        "title_ar": "تسجيل نشاط السحابة",
        "description_en": "The organization shall enable and monitor logging for all cloud service activities.",
        "description_ar": "يجب على الجهة تمكين ومراقبة التسجيل لجميع أنشطة الخدمات السحابية.",
        "priority": "HIGH",
    },
    {
        "control_id": "CSCC-5-2",
        "domain_en": "Security Monitoring",
        "domain_ar": "المراقبة الأمنية",
        "title_en": "Threat Detection",
        "title_ar": "الكشف عن التهديدات",
        "description_en": "The organization shall implement threat detection mechanisms for cloud environments.",
        "description_ar": "يجب على الجهة تطبيق آليات الكشف عن التهديدات لبيئات السحابة.",
        "priority": "CRITICAL",
    },
]
