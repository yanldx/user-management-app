describe('User management', () => {
  it('creates and deletes a user via the UI', () => {
    const email = `test${Date.now()}@example.com`
    cy.visit('/')
    cy.contains('label', 'First Name').parent().find('input').type('Test')
    cy.contains('label', 'Last Name').parent().find('input').type('User')
    cy.contains('label', 'Email').parent().find('input').type(email)
    cy.contains('label', 'Password').parent().find('input').type('secret')
    cy.contains('button', 'Create').click()

    cy.get('table').should('contain', email)

    cy.contains('tr', email).within(() => {
      cy.contains('button', 'Supprimer').click()
    })

    cy.get('table').should('not.contain', email)
  })
})
