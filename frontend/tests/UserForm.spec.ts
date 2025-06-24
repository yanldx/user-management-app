import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import UserForm from '../src/components/UserForm.vue'

global.fetch = vi.fn(() =>
  Promise.resolve({ json: () => Promise.resolve({}) })
) as any

describe('UserForm.vue', () => {
  it('envoie les données du formulaire', async () => {
    const wrapper = mount(UserForm)
    await wrapper.find('input[placeholder="Prénom"]').setValue('Loise')
    await wrapper.find('input[placeholder="Nom"]').setValue('Fenoll')
    await wrapper.find('input[placeholder="Email"]').setValue('loise@ynov.com')
    await wrapper.find('input[placeholder="Mot de passe"]').setValue('azerty')

    await wrapper.find('form').trigger('submit.prevent')

    expect(fetch).toHaveBeenCalledOnce()
    expect(fetch).toHaveBeenCalledWith(
      expect.stringContaining('/users/'),
      expect.objectContaining({
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          first_name: 'Loise',
          last_name: 'Fenoll',
          email: 'loise@ynov.com',
          password: 'azerty'
        })
      })
    )
  })
})
