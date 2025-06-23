describe('User management', () => {
  it('creates and lists a user', () => {
    const email = `test${Date.now()}@example.com`
    cy.visit('/')
    cy.get('[data-testid="first"]').type('Test')
    cy.get('[data-testid="last"]').type('User')
    cy.get('[data-testid="email"]').type(email)
    cy.get('[data-testid="password"]').type('secret')
    cy.get('[data-testid="submit"]').click()
    cy.contains('Refresh').click()
    cy.get('[data-testid="list"]').should('contain', email)
  })
})
