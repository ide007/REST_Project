import React from 'react'

function Header () {
    return(
        <section>
            <header>
                <nav>
                    <ul>
                        <li>Главная</li>
                        <li>Контент</li>
                        <li>
                            <form>
                                <input type="string" />
                                <button>Search</button>
                            </form>
                        </li>
                    </ul>
                    <hr/>
                </nav>
            </header>
        </section>
    )
}

export default Header
