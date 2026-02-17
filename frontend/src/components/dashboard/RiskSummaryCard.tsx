import { useTranslation } from 'react-i18next'
import { AlertTriangle } from 'lucide-react'

interface RiskSummaryCardProps {
  totalRisks: number
  openRisks: number
  criticalRisks: number
}

export default function RiskSummaryCard({ totalRisks, openRisks, criticalRisks }: RiskSummaryCardProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  return (
    <div className="rounded-lg border bg-card p-6">
      <div className="flex items-center gap-2 mb-4">
        <AlertTriangle className="h-5 w-5 text-orange-600" />
        <h3 className="text-lg font-semibold">{t('dashboard.openRisks')}</h3>
      </div>

      <div className="space-y-4">
        <div className="flex justify-between items-center">
          <span className="text-sm text-muted-foreground">
            {isArabic ? 'إجمالي المخاطر' : 'Total Risks'}
          </span>
          <span className="text-2xl font-bold">{totalRisks}</span>
        </div>

        <div className="flex justify-between items-center">
          <span className="text-sm text-muted-foreground">
            {isArabic ? 'المخاطر المفتوحة' : 'Open Risks'}
          </span>
          <span className="text-2xl font-bold text-orange-600">{openRisks}</span>
        </div>

        <div className="flex justify-between items-center pt-4 border-t">
          <span className="text-sm font-medium text-red-600">
            {isArabic ? 'مخاطر حرجة' : 'Critical Risks'}
          </span>
          <span className="text-2xl font-bold text-red-600">{criticalRisks}</span>
        </div>
      </div>
    </div>
  )
}
