import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { useCreateRisk } from '../../api/risks'
import { calculateRiskLevel, getRiskLevelColor } from '../../lib/utils'

interface RiskFormProps {
  onSuccess: () => void
  onCancel: () => void
}

export default function RiskForm({ onSuccess, onCancel }: RiskFormProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'
  const createRisk = useCreateRisk()

  const [formData, setFormData] = useState({
    title_en: '',
    title_ar: '',
    description_en: '',
    description_ar: '',
    asset: '',
    threat: '',
    vulnerability: '',
    impact_score: 3,
    likelihood_score: 3,
    treatment: 'MITIGATE',
    treatment_plan: '',
    owner_id: '', // This should come from user selection
  })

  const riskScore = formData.impact_score * formData.likelihood_score
  const riskLevel = calculateRiskLevel(formData.impact_score, formData.likelihood_score)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    try {
      await createRisk.mutateAsync(formData)
      onSuccess()
    } catch (error) {
      console.error('Failed to create risk:', error)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'العنوان (إنجليزي)' : 'Title (English)'}
          </label>
          <input
            type="text"
            value={formData.title_en}
            onChange={(e) => setFormData({ ...formData, title_en: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'العنوان (عربي)' : 'Title (Arabic)'}
          </label>
          <input
            type="text"
            value={formData.title_ar}
            onChange={(e) => setFormData({ ...formData, title_ar: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            dir="rtl"
            required
          />
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'الوصف (إنجليزي)' : 'Description (English)'}
          </label>
          <textarea
            value={formData.description_en}
            onChange={(e) => setFormData({ ...formData, description_en: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            rows={3}
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'الوصف (عربي)' : 'Description (Arabic)'}
          </label>
          <textarea
            value={formData.description_ar}
            onChange={(e) => setFormData({ ...formData, description_ar: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            rows={3}
            dir="rtl"
            required
          />
        </div>
      </div>

      <div className="grid md:grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'الأصل' : 'Asset'}
          </label>
          <input
            type="text"
            value={formData.asset}
            onChange={(e) => setFormData({ ...formData, asset: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'التهديد' : 'Threat'}
          </label>
          <input
            type="text"
            value={formData.threat}
            onChange={(e) => setFormData({ ...formData, threat: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'الثغرة' : 'Vulnerability'}
          </label>
          <input
            type="text"
            value={formData.vulnerability}
            onChange={(e) => setFormData({ ...formData, vulnerability: e.target.value })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
            required
          />
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'درجة التأثير (1-5)' : 'Impact Score (1-5)'}
          </label>
          <select
            value={formData.impact_score}
            onChange={(e) => setFormData({ ...formData, impact_score: parseInt(e.target.value) })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
          >
            {[1, 2, 3, 4, 5].map(score => (
              <option key={score} value={score}>{score}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            {isArabic ? 'درجة الاحتمالية (1-5)' : 'Likelihood Score (1-5)'}
          </label>
          <select
            value={formData.likelihood_score}
            onChange={(e) => setFormData({ ...formData, likelihood_score: parseInt(e.target.value) })}
            className="w-full rounded-md border bg-background px-3 py-2 text-sm"
          >
            {[1, 2, 3, 4, 5].map(score => (
              <option key={score} value={score}>{score}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Risk calculation display */}
      <div className="rounded-lg border p-4 bg-muted">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium">
              {isArabic ? 'درجة المخاطرة المحسوبة' : 'Calculated Risk Score'}
            </p>
            <p className="text-2xl font-bold">{riskScore}</p>
          </div>
          <div>
            <span className={`px-3 py-1 rounded-full text-white text-sm font-medium ${getRiskLevelColor(riskLevel)}`}>
              {riskLevel}
            </span>
          </div>
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium mb-2">
          {isArabic ? 'استراتيجية المعالجة' : 'Treatment Strategy'}
        </label>
        <select
          value={formData.treatment}
          onChange={(e) => setFormData({ ...formData, treatment: e.target.value })}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm"
        >
          <option value="ACCEPT">{isArabic ? 'قبول' : 'Accept'}</option>
          <option value="MITIGATE">{isArabic ? 'تخفيف' : 'Mitigate'}</option>
          <option value="TRANSFER">{isArabic ? 'نقل' : 'Transfer'}</option>
          <option value="AVOID">{isArabic ? 'تجنب' : 'Avoid'}</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium mb-2">
          {isArabic ? 'خطة المعالجة' : 'Treatment Plan'}
        </label>
        <textarea
          value={formData.treatment_plan}
          onChange={(e) => setFormData({ ...formData, treatment_plan: e.target.value })}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm"
          rows={3}
        />
      </div>

      <div className="flex gap-2 justify-end">
        <button
          type="button"
          onClick={onCancel}
          className="px-4 py-2 rounded-md border text-sm font-medium hover:bg-accent"
        >
          {t('common.cancel')}
        </button>
        <button
          type="submit"
          disabled={createRisk.isPending}
          className="px-4 py-2 rounded-md bg-primary text-primary-foreground text-sm font-medium hover:bg-primary/90 disabled:opacity-50"
        >
          {createRisk.isPending ? t('common.loading') : t('common.save')}
        </button>
      </div>
    </form>
  )
}
