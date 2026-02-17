import { Link, useLocation } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { LayoutDashboard, Shield, AlertTriangle, ClipboardCheck } from 'lucide-react'
import { cn } from '../../lib/utils'

const navigation = [
  { name: 'nav.dashboard', to: '/dashboard', icon: LayoutDashboard },
  { name: 'nav.compliance', to: '/compliance', icon: Shield },
  { name: 'nav.risks', to: '/risks', icon: AlertTriangle },
  { name: 'nav.audits', to: '/audits', icon: ClipboardCheck },
]

export default function Sidebar() {
  const location = useLocation()
  const { t } = useTranslation()

  return (
    <aside className="w-64 border-e bg-card">
      <div className="flex h-16 items-center border-b px-6">
        <h1 className="text-xl font-bold">{t('app.name')}</h1>
      </div>
      <nav className="space-y-1 p-4">
        {navigation.map((item) => {
          const Icon = item.icon
          const isActive = location.pathname === item.to

          return (
            <Link
              key={item.to}
              to={item.to}
              className={cn(
                'flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-primary text-primary-foreground'
                  : 'text-muted-foreground hover:bg-accent hover:text-accent-foreground'
              )}
            >
              <Icon className="h-5 w-5" />
              {t(item.name)}
            </Link>
          )
        })}
      </nav>
    </aside>
  )
}
