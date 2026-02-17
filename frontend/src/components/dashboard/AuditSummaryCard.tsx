import { useTranslation } from 'react-i18next'
import { ClipboardCheck } from 'lucide-react'

interface AuditSummaryCardProps {
  totalAudits: number
  activeAudits: number
  openFindings: number
}

export default function AuditSummaryCard({ totalAudits, activeAudits, openFindings }: AuditSummaryCardProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  return (
    <div className="rounded-lg border bg-card p-6">
      <div className="flex items-center gap-2 mb-4">
        <ClipboardCheck className="h-5 w-5 text-blue-600" />
        <h3 className="text-lg font-semibold">{t('dashboard.pendingAudits')}</h3>
      </div>

      <div className="space-y-4">
        <div className="flex justify-between items-center">
          <span className="text-sm text-muted-foreground">
            {isArabic ? 'إجمالي التدقيقات' : 'Total Audits'}
          </span>
          <span className="text-2xl font-bold">{totalAudits}</span>
        </div>

        <div className="flex justify-between items-center">
          <span className="text-sm text-muted-foreground">
            {isArabic ? 'التدقيقات النشطة' : 'Active Audits'}
          </span>
          <span className="text-2xl font-bold text-blue-600">{activeAudits}</span>
        </div>

        <div className="flex justify-between items-center pt-4 border-t">
          <span className="text-sm font-medium text-orange-600">
            {isArabic ? 'نتائج مفتوحة' : 'Open Findings'}
          </span>
          <span className="text-2xl font-bold text-orange-600">{openFindings}</span>
        </div>
      </div>
    </div>
  )
}
