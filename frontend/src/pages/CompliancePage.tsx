import { useTranslation } from 'react-i18next'

export default function CompliancePage() {
  const { t } = useTranslation()

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">{t('compliance.title')}</h1>

      <div className="rounded-lg border bg-card p-6">
        <p className="text-muted-foreground">
          Compliance management module - Controls and evidence tracking
        </p>
      </div>
    </div>
  )
}
