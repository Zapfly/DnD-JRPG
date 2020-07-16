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


describe("App testing block", () => {
  
    test('attack button calls a function', async () => {
      act(() => {
        render(
          <ContextProvider>
            <CombatComp />
          </ContextProvider>
        );
      })
  
      // document.getElementById("monster 0").classList.add('selected')
        
      
      expect(document.getElementById('HPBar 0').style._values.width).toEqual('100%')
        
      expect(screen.getAllByRole("monster")[0]).not.toHaveClass("selected")
      act(() => {
  
        fireEvent.click(
          screen.getAllByRole("monster")[0]
        )
      })       
      expect(screen.getAllByRole("monster")[0]).toHaveClass("selected")
  
      act(() => {
  
        fireEvent.click(
          screen.getByText("Attack")
        )
      })
  
      expect(document.getElementById('HPBar 0').style._values.width).not.toEqual('100%')
    })
  
  
  })
  