import { useMemo } from 'react'
import { useTranslation } from 'react-i18next'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts'

interface Risk {
  id: string
  risk_level: string
  status: string
}

interface RiskHeatmapProps {
  risks: Risk[]
}

export default function RiskHeatmap({ risks }: RiskHeatmapProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  const heatmapData = useMemo(() => {
    const levels = ['VERY_LOW', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
    const levelNames: Record<string, string> = {
      VERY_LOW: isArabic ? 'منخفض جداً' : 'Very Low',
      LOW: isArabic ? 'منخفض' : 'Low',
      MEDIUM: isArabic ? 'متوسط' : 'Medium',
      HIGH: isArabic ? 'عالي' : 'High',
      CRITICAL: isArabic ? 'حرج' : 'Critical',
    }

    return levels.map(level => {
      const levelRisks = risks.filter(r => r.risk_level === level)
      const openRisks = levelRisks.filter(r => r.status === 'OPEN').length
      const closedRisks = levelRisks.filter(r => r.status === 'CLOSED').length

      return {
        level: levelNames[level],
        levelKey: level,
        open: openRisks,
        closed: closedRisks,
        total: levelRisks.length,
      }
    })
  }, [risks, isArabic])

  const getBarColor = (levelKey: string): string => {
    const colors: Record<string, string> = {
      VERY_LOW: '#22c55e',
      LOW: '#3b82f6',
      MEDIUM: '#eab308',
      HIGH: '#f97316',
      CRITICAL: '#ef4444',
    }
    return colors[levelKey] || '#6b7280'
  }

  return (
    <div className="rounded-lg border bg-card p-6">
      <h3 className="text-lg font-semibold mb-4">
        {isArabic ? 'توزيع المخاطر حسب المستوى' : 'Risk Distribution by Level'}
      </h3>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={heatmapData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="level" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar 
            dataKey="open" 
            name={isArabic ? 'مفتوح' : 'Open'}
            stackId="a"
          >
            {heatmapData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={getBarColor(entry.levelKey)} opacity={0.8} />
            ))}
          </Bar>
          <Bar 
            dataKey="closed" 
            name={isArabic ? 'مغلق' : 'Closed'}
            stackId="a"
            fill="#9ca3af"
            opacity={0.5}
          />
        </BarChart>
      </ResponsiveContainer>

      {/* Summary stats */}
      <div className="mt-4 grid grid-cols-2 md:grid-cols-5 gap-2">
        {heatmapData.map(item => (
          <div key={item.levelKey} className="text-center p-2 rounded border">
            <div className="text-2xl font-bold" style={{ color: getBarColor(item.levelKey) }}>
              {item.total}
            </div>
            <div className="text-xs text-muted-foreground">{item.level}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
