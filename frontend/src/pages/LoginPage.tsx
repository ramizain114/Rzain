import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import { useLogin, useGetProfile } from '../api/auth'
import { useAuthStore } from '../stores/auth-store'

export default function LoginPage() {
  const { t } = useTranslation()
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const { setAuth } = useAuthStore()
  const loginMutation = useLogin()
  const profileMutation = useGetProfile()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')

    try {
      const loginResponse = await loginMutation.mutateAsync({ username, password })
      const profile = await profileMutation.mutateAsync()

      setAuth(profile, loginResponse.access_token)
      navigate('/dashboard')
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed')
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-background">
      <div className="w-full max-w-md space-y-8 rounded-lg border bg-card p-8 shadow-lg">
        <div className="text-center">
          <h1 className="text-3xl font-bold">{t('app.name')}</h1>
          <p className="mt-2 text-sm text-muted-foreground">{t('auth.welcomeBack')}</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          {error && (
            <div className="rounded-md bg-destructive/10 p-3 text-sm text-destructive">
              {error}
            </div>
          )}

          <div>
            <label htmlFor="username" className="block text-sm font-medium mb-2">
              {t('auth.username')}
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full rounded-md border bg-background px-3 py-2 text-sm"
              required
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-sm font-medium mb-2">
              {t('auth.password')}
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-md border bg-background px-3 py-2 text-sm"
              required
            />
          </div>

          <button
            type="submit"
            disabled={loginMutation.isPending}
            className="w-full rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
          >
            {loginMutation.isPending ? t('common.loading') : t('auth.login')}
          </button>
        </form>
      </div>
    </div>
  )
}
