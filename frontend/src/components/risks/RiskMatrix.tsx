import { useMemo } from 'react'
import { useTranslation } from 'react-i18next'
import { getRiskLevelColor } from '../../lib/utils'

interface Risk {
  id: string
  risk_id: string
  title_en: string
  title_ar: string
  impact_score: number
  likelihood_score: number
  risk_level: string
}

interface RiskMatrixProps {
  risks: Risk[]
}

export default function RiskMatrix({ risks }: RiskMatrixProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  // Group risks by impact and likelihood
  const matrixData = useMemo(() => {
    const matrix: Record<string, Risk[]> = {}
    
    for (let impact = 5; impact >= 1; impact--) {
      for (let likelihood = 1; likelihood <= 5; likelihood++) {
        const key = `${impact}-${likelihood}`
        matrix[key] = risks.filter(
          r => r.impact_score === impact && r.likelihood_score === likelihood
        )
      }
    }
    
    return matrix
  }, [risks])

  const getCellColor = (impact: number, likelihood: number): string => {
    const score = impact * likelihood
    if (score <= 3) return 'bg-green-100 hover:bg-green-200'
    if (score <= 6) return 'bg-blue-100 hover:bg-blue-200'
    if (score <= 12) return 'bg-yellow-100 hover:bg-yellow-200'
    if (score <= 20) return 'bg-orange-100 hover:bg-orange-200'
    return 'bg-red-100 hover:bg-red-200'
  }

  return (
    <div className="rounded-lg border bg-card p-6">
      <h3 className="text-lg font-semibold mb-4">
        {isArabic ? 'مصفوفة المخاطر 5×5' : 'Risk Matrix 5×5'}
      </h3>

      <div className="overflow-x-auto">
        <div className="inline-block min-w-full">
          {/* Matrix Header */}
          <div className="flex mb-2">
            <div className="w-24"></div>
            <div className="flex-1 text-center text-sm font-medium mb-2" dir="ltr">
              {isArabic ? 'الاحتمالية →' : 'Likelihood →'}
            </div>
          </div>

          {/* Likelihood labels */}
          <div className="flex">
            <div className="w-24 flex items-center justify-center">
              <div className="transform -rotate-90 whitespace-nowrap text-sm font-medium">
                {isArabic ? 'التأثير ↑' : 'Impact ↑'}
              </div>
            </div>
            <div className="flex-1">
              <div className="grid grid-cols-5 gap-1 mb-1">
                {[1, 2, 3, 4, 5].map(score => (
                  <div key={score} className="text-center text-xs font-medium p-1">
                    {score}
                  </div>
                ))}
              </div>

              {/* Matrix cells */}
              {[5, 4, 3, 2, 1].map(impact => (
                <div key={impact} className="flex gap-1 mb-1">
                  {[1, 2, 3, 4, 5].map(likelihood => {
                    const key = `${impact}-${likelihood}`
                    const cellRisks = matrixData[key] || []
                    const score = impact * likelihood

                    return (
                      <div
                        key={key}
                        className={`flex-1 aspect-square border rounded p-2 transition-colors cursor-pointer ${getCellColor(impact, likelihood)}`}
                        title={`Impact: ${impact}, Likelihood: ${likelihood}, Score: ${score}, Risks: ${cellRisks.length}`}
                      >
                        <div className="text-xs font-bold text-center">
                          {score}
                        </div>
                        {cellRisks.length > 0 && (
                          <div className="text-xs text-center mt-1">
                            {cellRisks.length} {isArabic ? 'مخاطر' : 'risks'}
                          </div>
                        )}
                      </div>
                    )
                  })}
                </div>
              ))}

              {/* Impact labels on right side */}
              <div className="flex gap-1 mt-1">
                {[5, 4, 3, 2, 1].map(score => (
                  <div key={score} className="flex-1 text-center text-xs font-medium p-1">
                    {/* Empty space for alignment */}
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Legend */}
          <div className="mt-6 flex flex-wrap gap-4 justify-center text-xs">
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-green-100 border rounded"></div>
              <span>{isArabic ? 'منخفض جداً (1-3)' : 'Very Low (1-3)'}</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-blue-100 border rounded"></div>
              <span>{isArabic ? 'منخفض (4-6)' : 'Low (4-6)'}</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-yellow-100 border rounded"></div>
              <span>{isArabic ? 'متوسط (7-12)' : 'Medium (7-12)'}</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-orange-100 border rounded"></div>
              <span>{isArabic ? 'عالي (13-20)' : 'High (13-20)'}</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 bg-red-100 border rounded"></div>
              <span>{isArabic ? 'حرج (21-25)' : 'Critical (21-25)'}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
