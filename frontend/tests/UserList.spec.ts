import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import UserList from '../src/components/UserList.vue'

describe('UserList.vue', () => {
  it('affiche les utilisateurs', () => {
    const wrapper = mount(UserList, {
      props: {
        users: [
          { id: 1, first_name: 'Loise', last_name: 'Fenoll', email: 'loise@ynov.com' }
        ],
        isAdmin: true
      }
    })

    expect(wrapper.text()).toContain('Loise Fenoll')
    expect(wrapper.text()).toContain('loise@ynov.com')
  })
})
