import { useTranslation } from 'react-i18next'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

interface TrendPoint {
  date: string
  percentage: number
  implemented_count: number
  total_count: number
}

interface ComplianceTrendChartProps {
  data: TrendPoint[]
}

export default function ComplianceTrendChart({ data }: ComplianceTrendChartProps) {
  const { t, i18n } = useTranslation()
  const isArabic = i18n.language === 'ar'

  return (
    <div className="rounded-lg border bg-card p-6">
      <h3 className="text-lg font-semibold mb-4">
        {isArabic ? 'اتجاه الامتثال (30 يوماً)' : 'Compliance Trend (30 Days)'}
      </h3>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            tick={{ fontSize: 12 }}
            tickFormatter={(value) => {
              const date = new Date(value)
              return `${date.getMonth() + 1}/${date.getDate()}`
            }}
          />
          <YAxis domain={[0, 100]} />
          <Tooltip 
            formatter={(value: number) => `${value.toFixed(1)}%`}
            labelFormatter={(label) => isArabic ? `التاريخ: ${label}` : `Date: ${label}`}
          />
          <Legend />
          <Line
            type="monotone"
            dataKey="percentage"
            name={isArabic ? 'نسبة الامتثال' : 'Compliance %'}
            stroke="#3b82f6"
            strokeWidth={2}
            dot={{ r: 3 }}
            activeDot={{ r: 5 }}
          />
        </LineChart>
      </ResponsiveContainer>

      {data.length > 0 && (
        <div className="mt-4 flex justify-between text-sm text-muted-foreground">
          <span>
            {isArabic ? 'البداية:' : 'Start:'} {data[0].percentage.toFixed(1)}%
          </span>
          <span>
            {isArabic ? 'الحالي:' : 'Current:'} {data[data.length - 1].percentage.toFixed(1)}%
          </span>
        </div>
      )}
    </div>
  )
}
