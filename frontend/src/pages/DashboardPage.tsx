import { useTranslation } from 'react-i18next'

export default function DashboardPage() {
  const { t } = useTranslation()

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">{t('dashboard.title')}</h1>

      <div className="grid gap-6 md:grid-cols-3">
        <div className="rounded-lg border bg-card p-6">
          <h3 className="text-sm font-medium text-muted-foreground">
            {t('dashboard.complianceScore')}
          </h3>
          <p className="mt-2 text-3xl font-bold">85%</p>
        </div>

        <div className="rounded-lg border bg-card p-6">
          <h3 className="text-sm font-medium text-muted-foreground">
            {t('dashboard.openRisks')}
          </h3>
          <p className="mt-2 text-3xl font-bold">12</p>
        </div>

        <div className="rounded-lg border bg-card p-6">
          <h3 className="text-sm font-medium text-muted-foreground">
            {t('dashboard.pendingAudits')}
          </h3>
          <p className="mt-2 text-3xl font-bold">3</p>
        </div>
      </div>

      <div className="rounded-lg border bg-card p-6">
        <h2 className="text-xl font-semibold mb-4">{t('dashboard.overview')}</h2>
        <p className="text-muted-foreground">
          Welcome to Amana-GRC. Use the navigation menu to access different modules.
        </p>
      </div>
    </div>
  )
}
