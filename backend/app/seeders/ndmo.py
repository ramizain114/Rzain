"""NDMO Data Management Standards seeder.

Based on Saudi National Data Management Office standards for data governance.
"""

STANDARD_META = {
    "code": "NDMO",
    "name_en": "Data Management Standards",
    "name_ar": "معايير إدارة البيانات",
    "description_en": "National Data Management Office standards for data governance and management",
    "description_ar": "معايير المكتب الوطني لإدارة البيانات لحوكمة وإدارة البيانات",
    "version": "1.0",
    "category": "data_management",
}

CONTROLS = [
    # Data Governance
    {
        "control_id": "NDMO-1-1",
        "domain_en": "Data Governance",
        "domain_ar": "حوكمة البيانات",
        "title_en": "Data Governance Framework",
        "title_ar": "إطار حوكمة البيانات",
        "description_en": "The organization shall establish and maintain a data governance framework defining roles, policies, and procedures.",
        "description_ar": "يجب على الجهة إنشاء والحفاظ على إطار حوكمة البيانات الذي يحدد الأدوار والسياسات والإجراءات.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "NDMO-1-2",
        "domain_en": "Data Governance",
        "domain_ar": "حوكمة البيانات",
        "title_en": "Data Stewardship",
        "title_ar": "الوصاية على البيانات",
        "description_en": "The organization shall assign data stewards responsible for data quality and lifecycle management.",
        "description_ar": "يجب على الجهة تعيين وصي البيانات المسؤولين عن جودة البيانات وإدارة دورة حياتها.",
        "priority": "HIGH",
    },
    
    # Data Classification
    {
        "control_id": "NDMO-2-1",
        "domain_en": "Data Classification",
        "domain_ar": "تصنيف البيانات",
        "title_en": "Data Classification Policy",
        "title_ar": "سياسة تصنيف البيانات",
        "description_en": "The organization shall classify data based on sensitivity, criticality, and regulatory requirements.",
        "description_ar": "يجب على الجهة تصنيف البيانات بناءً على الحساسية والأهمية الحرجة والمتطلبات التنظيمية.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "NDMO-2-2",
        "domain_en": "Data Classification",
        "domain_ar": "تصنيف البيانات",
        "title_en": "Data Labeling",
        "title_ar": "وسم البيانات",
        "description_en": "The organization shall implement data labeling mechanisms to identify classification levels.",
        "description_ar": "يجب على الجهة تطبيق آليات وسم البيانات لتحديد مستويات التصنيف.",
        "priority": "MEDIUM",
    },
    
    # Data Quality
    {
        "control_id": "NDMO-3-1",
        "domain_en": "Data Quality",
        "domain_ar": "جودة البيانات",
        "title_en": "Data Quality Standards",
        "title_ar": "معايير جودة البيانات",
        "description_en": "The organization shall define and enforce data quality standards including accuracy, completeness, and timeliness.",
        "description_ar": "يجب على الجهة تحديد وفرض معايير جودة البيانات بما في ذلك الدقة والاكتمال والتوقيت المناسب.",
        "priority": "HIGH",
    },
    {
        "control_id": "NDMO-3-2",
        "domain_en": "Data Quality",
        "domain_ar": "جودة البيانات",
        "title_en": "Data Quality Monitoring",
        "title_ar": "مراقبة جودة البيانات",
        "description_en": "The organization shall regularly monitor and report on data quality metrics.",
        "description_ar": "يجب على الجهة مراقبة والإبلاغ عن مقاييس جودة البيانات بانتظام.",
        "priority": "MEDIUM",
    },
    
    # Data Lifecycle Management
    {
        "control_id": "NDMO-4-1",
        "domain_en": "Lifecycle Management",
        "domain_ar": "إدارة دورة الحياة",
        "title_en": "Data Retention Policy",
        "title_ar": "سياسة الاحتفاظ بالبيانات",
        "description_en": "The organization shall define and implement data retention policies aligned with legal and business requirements.",
        "description_ar": "يجب على الجهة تحديد وتنفيذ سياسات الاحتفاظ بالبيانات متوافقة مع المتطلبات القانونية والتجارية.",
        "priority": "HIGH",
    },
    {
        "control_id": "NDMO-4-2",
        "domain_en": "Lifecycle Management",
        "domain_ar": "إدارة دورة الحياة",
        "title_en": "Data Disposal",
        "title_ar": "التخلص من البيانات",
        "description_en": "The organization shall securely dispose of data when no longer needed according to retention policies.",
        "description_ar": "يجب على الجهة التخلص الآمن من البيانات عند عدم الحاجة إليها وفقًا لسياسات الاحتفاظ.",
        "priority": "HIGH",
    },
    
    # Data Privacy
    {
        "control_id": "NDMO-5-1",
        "domain_en": "Data Privacy",
        "domain_ar": "خصوصية البيانات",
        "title_en": "Privacy Impact Assessment",
        "title_ar": "تقييم تأثير الخصوصية",
        "description_en": "The organization shall conduct privacy impact assessments for systems processing personal data.",
        "description_ar": "يجب على الجهة إجراء تقييمات تأثير الخصوصية للأنظمة التي تعالج البيانات الشخصية.",
        "priority": "HIGH",
    },
    {
        "control_id": "NDMO-5-2",
        "domain_en": "Data Privacy",
        "domain_ar": "خصوصية البيانات",
        "title_en": "Consent Management",
        "title_ar": "إدارة الموافقة",
        "description_en": "The organization shall implement mechanisms to obtain, record, and manage data subject consent.",
        "description_ar": "يجب على الجهة تطبيق آليات للحصول على موافقة صاحب البيانات وتسجيلها وإدارتها.",
        "priority": "CRITICAL",
    },
    
    # Data Sharing
    {
        "control_id": "NDMO-6-1",
        "domain_en": "Data Sharing",
        "domain_ar": "مشاركة البيانات",
        "title_en": "Data Sharing Agreement",
        "title_ar": "اتفاقية مشاركة البيانات",
        "description_en": "The organization shall establish formal agreements before sharing data with external parties.",
        "description_ar": "يجب على الجهة إنشاء اتفاقيات رسمية قبل مشاركة البيانات مع أطراف خارجية.",
        "priority": "HIGH",
    },
    {
        "control_id": "NDMO-6-2",
        "domain_en": "Data Sharing",
        "domain_ar": "مشاركة البيانات",
        "title_en": "Data Anonymization",
        "title_ar": "إخفاء هوية البيانات",
        "description_en": "The organization shall anonymize or pseudonymize data before sharing when appropriate.",
        "description_ar": "يجب على الجهة إخفاء هوية البيانات أو استخدام أسماء مستعارة قبل المشاركة عند الاقتضاء.",
        "priority": "MEDIUM",
    },
]
