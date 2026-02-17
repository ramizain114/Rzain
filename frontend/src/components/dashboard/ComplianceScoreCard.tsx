import { useTranslation } from 'react-i18next'
import { Shield, TrendingUp } from 'lucide-react'

interface ComplianceScoreCardProps {
  percentage: number
  total: number
  implemented: number
}

export default function ComplianceScoreCard({ percentage, total, implemented }: ComplianceScoreCardProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  const getScoreColor = (score: number) => {
    if (score >= 90) return 'text-green-600'
    if (score >= 70) return 'text-yellow-600'
    if (score >= 50) return 'text-orange-600'
    return 'text-red-600'
  }

  const getProgressColor = (score: number) => {
    if (score >= 90) return 'bg-green-600'
    if (score >= 70) return 'bg-yellow-600'
    if (score >= 50) return 'bg-orange-600'
    return 'bg-red-600'
  }

  return (
    <div className="rounded-lg border bg-card p-6">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Shield className="h-5 w-5 text-primary" />
          <h3 className="text-lg font-semibold">{t('dashboard.complianceScore')}</h3>
        </div>
        <TrendingUp className="h-4 w-4 text-muted-foreground" />
      </div>

      <div className="text-center">
        <div className={`text-5xl font-bold ${getScoreColor(percentage)}`}>
          {percentage.toFixed(1)}%
        </div>
        <p className="text-sm text-muted-foreground mt-2">
          {implemented} {isArabic ? 'من' : 'of'} {total} {isArabic ? 'ضوابط منفذة' : 'controls implemented'}
        </p>
      </div>

      <div className="mt-4">
        <div className="w-full bg-muted rounded-full h-2">
          <div
            className={`h-2 rounded-full transition-all ${getProgressColor(percentage)}`}
            style={{ width: `${percentage}%` }}
          ></div>
        </div>
      </div>
    </div>
  )
}
