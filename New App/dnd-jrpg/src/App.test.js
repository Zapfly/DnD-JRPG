import React from 'react';
import { render, fireEvent, waitFor, screen, getByText, waitForElement } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';
import { ContextProvider, AppContext } from './AppContext.js';
import '@testing-library/jest-dom';
import HeroComp from './Components/HeroComp/HeroComp';
import Herc from './images/Herccolored.png';
import { Arena } from './scripts/combat.js';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
import MonsterComp from './Components/MonsterComp/MonsterComp';
import CombatComp from './Components/CombatComp/CombatComp';
import { /*render,*/ unmountComponentAtNode } from "react-dom";
import { act } from 'react-dom/test-utils';

// "@testing-library/jest-dom": "^4.2.4",
//     "@testing-library/react": "^9.5.0",
//     "@testing-library/user-event": "^7.2.1",

describe("App testing block", () => {
  let container = null;

  beforeEach(() => {
    container = document.createElement("div");
    document.body.appendChild(container);
  });

  afterEach(() => {
    unmountComponentAtNode(container);
    container.remove();
    container = null;

  });

  test('renders learn react link', () => {
    act(()=> {  
      const { getByText } = render(
          <App />, container
    )
      const linkElement = getByText(/Monster Dungeon/i);
      expect(linkElement).toBeInTheDocument();
    })
  });

  test('renders HeroComp', () => {
    const arena = new Arena();
    arena.createHero("Hercules", 30, 40, Herc)

    act(() => {
      render(<HeroComp
        heroInfo = {arena.combatants[0]}
        />, container)

    })
    expect(screen.getByRole('playerCharacter')).toBeInTheDocument(true)
  });

  test('render MonsterComp', () => {
    const arena1 = new Arena();
    arena1.createMonster("Boblin", 1, 1, Gobo)

    act(()=>{
      render(
        <ContextProvider >
            <MonsterComp
              monsterInfo = {arena1.combatants[0]}
              key={0}
              index={0}
              monsters={arena1.monsters}
            />
        </ContextProvider>,
        container
        )
    }
    )

    expect(screen.getByRole('monster')).toBeInTheDocument(true)

  });

  test('renders Monster array', () => {

    act(()=> {     
      render(
        <ContextProvider>
          <CombatComp/>
        </ContextProvider>,
        container
        );
    })

    
    expect(screen.getAllByRole("monster")).not.toHaveLength(0);
    expect(screen.getByRole('monsterContainer')).toBeInTheDocument(true);
    expect(screen.getAllByRole('monsterContainer')).toHaveLength(1);
    
  });

  test('clicking monster sets class to "selected"', () => {

    act(()=> {     
      render(
        <ContextProvider>
          <CombatComp/>
        </ContextProvider>,
        container
        );
    })

    expect(screen.getAllByRole("monster")[0]).not.toHaveClass("selected")
    fireEvent.click(
      screen.getAllByRole("monster")[0]
    )
    expect(screen.getAllByRole("monster")[0]).toHaveClass("selected")

    fireEvent.click(
      screen.getAllByRole("monster")[1]
    )
    expect(screen.getAllByRole("monster")[0]).not.toHaveClass("selected")
    expect(screen.getAllByRole("monster")[1]).toHaveClass("selected")
  })

  test('attack button calls a function', async () => {
    act(() => {
      render(
        <ContextProvider>
          <CombatComp />
        </ContextProvider>,
        container
      );
    })

    document.getElementById("monster 0").classList.add('selected')
      
    expect(screen.getAllByRole("monster")[0]).toHaveClass("selected")
   
    expect(document.getElementById('HPBar 0').style._values.width).toEqual('100%')
    // await waitFor(() => {
    //   fireEvent.click(
    //     screen.getAllByRole("monster")[0]
    //   )  
    // })

    // await waitFor(async () => {

    //   await setTimeout(
    //     fireEvent.click(
    //       screen.getByRole("AttackButton")
    //     ), 3000)
    // })

    act(() => {

      
      userEvent.click(
        screen.getByText("Attack")
        )
    })

    expect(document.getElementById('HPBar 0').style._values.width).not.toEqual('100%')
    // await waitFor(() => {
    // })
      
      // expect(mockFn).toHaveBeenCalled()
  })
})
