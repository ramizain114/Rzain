import { useTranslation } from 'react-i18next'
import { useDashboardSummary } from '../api/dashboard'
import ComplianceScoreCard from '../components/dashboard/ComplianceScoreCard'
import RiskSummaryCard from '../components/dashboard/RiskSummaryCard'
import AuditSummaryCard from '../components/dashboard/AuditSummaryCard'

export default function DashboardPage() {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'
  const { data: summary, isLoading } = useDashboardSummary()

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-muted-foreground">{t('common.loading')}</div>
      </div>
    )
  }

  if (!summary) {
    return null
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">{t('dashboard.title')}</h1>
        <div className="text-sm text-muted-foreground">
          {isArabic ? 'آخر تحديث: الآن' : 'Last updated: Now'}
        </div>
      </div>

      {/* Key metrics */}
      <div className="grid gap-6 md:grid-cols-3">
        <ComplianceScoreCard
          percentage={summary.compliance_percentage}
          total={summary.total_controls}
          implemented={summary.implemented_controls}
        />
        
        <RiskSummaryCard
          totalRisks={summary.total_risks}
          openRisks={summary.open_risks}
          criticalRisks={summary.critical_risks}
        />
        
        <AuditSummaryCard
          totalAudits={summary.total_audits}
          activeAudits={summary.active_audits}
          openFindings={summary.open_findings}
        />
      </div>

      {/* Quick overview */}
      <div className="rounded-lg border bg-card p-6">
        <h2 className="text-xl font-semibold mb-4">{t('dashboard.overview')}</h2>
        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <h3 className="text-sm font-medium mb-2">
              {isArabic ? 'حالة الامتثال' : 'Compliance Status'}
            </h3>
            <p className="text-sm text-muted-foreground">
              {isArabic 
                ? `${summary.implemented_controls} من ${summary.total_controls} ضابط منفذ (${summary.compliance_percentage}%)`
                : `${summary.implemented_controls} of ${summary.total_controls} controls implemented (${summary.compliance_percentage}%)`
              }
            </p>
          </div>
          <div>
            <h3 className="text-sm font-medium mb-2">
              {isArabic ? 'حالة المخاطر' : 'Risk Status'}
            </h3>
            <p className="text-sm text-muted-foreground">
              {isArabic
                ? `${summary.open_risks} مخاطر مفتوحة، ${summary.critical_risks} حرجة`
                : `${summary.open_risks} open risks, ${summary.critical_risks} critical`
              }
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
