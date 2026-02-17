import { useTranslation } from 'react-i18next'

export default function AuditPage() {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">{t('nav.audits')}</h1>

      <div className="rounded-lg border bg-card p-6">
        <h2 className="text-xl font-semibold mb-4">
          {isArabic ? 'سير عمل التدقيق' : 'Audit Workflow'}
        </h2>
        <p className="text-muted-foreground">
          {isArabic 
            ? 'إدارة عمليات التدقيق والنتائج والإجراءات التصحيحية'
            : 'Manage audit processes, findings, and corrective actions'}
        </p>
        
        <div className="mt-6 grid md:grid-cols-4 gap-4">
          <div className="p-4 rounded-lg border bg-blue-50">
            <div className="text-2xl font-bold text-blue-600">2</div>
            <div className="text-sm text-muted-foreground">
              {isArabic ? 'مخطط' : 'Planned'}
            </div>
          </div>
          <div className="p-4 rounded-lg border bg-yellow-50">
            <div className="text-2xl font-bold text-yellow-600">3</div>
            <div className="text-sm text-muted-foreground">
              {isArabic ? 'قيد التنفيذ' : 'In Progress'}
            </div>
          </div>
          <div className="p-4 rounded-lg border bg-green-50">
            <div className="text-2xl font-bold text-green-600">5</div>
            <div className="text-sm text-muted-foreground">
              {isArabic ? 'مكتمل' : 'Completed'}
            </div>
          </div>
          <div className="p-4 rounded-lg border bg-gray-50">
            <div className="text-2xl font-bold text-gray-600">8</div>
            <div className="text-sm text-muted-foreground">
              {isArabic ? 'مغلق' : 'Closed'}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
