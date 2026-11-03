# PROG101 — Digital Healthcare Patient Data Management System

Project: Digital Healthcare Patient Data Management System (DHPDMS)  
Student: Alex Alimamy Debe Kamara
Student ID: 905006307  
Course: PROG101 — Principles of Programming Logic and Design  
Institution: Limkokwing University of Creative Technology, Sierra Leone  
Examiner: Elijah Fullah  

## Overview

DHPDMS is a classroom logic prototype for a lightweight, offline-first digital patient-record workflow in Sierra Leone. It supports patient registration, record search, diagnosis/treatment updates, input validation, and a repeating menu. It is designed to demonstrate sequence, selection, repetition, functions, modularity, and array searching.

## Problem solve 
The Digital Healthcare Patient Data Management System (DHPDMS) solves the problem of inefficient, paper-based patient record-keeping in Sierra Leone clinics by providing a lightweight, offline-first digital solution.
Key aspects of the problem and its solution include:
 * The Problem: Traditional paper records are prone to physical loss, slow retrieval times, and human error during patient intake and medical history tracking.
 * The Solution: A structured, console-based digital application that enables fast patient registration, instant record searching via unique IDs, and secure diagnosis/treatment updates.
 * Impact: Streamlines clinic workflows, minimizes administrative errors, and supports local healthcare infrastructure aligned with Sustainable Development Goals (SDG 3 and SDG 9).
 * 

## SDG alignment

- SDG 3 — Good Health and Well-being: supports faster retrieval and continuity of health information.
- SDG 9 — Industry, Innovation and Infrastructure: demonstrates adaptable, open digital infrastructure for public services.

## Modules

- `Main` — controls the menu loop.
- `RegisterPatient` — validates and stores new demographic and medical information.
- `SearchPatient` — searches the patient-ID array and displays a matching record.
- `UpdateRecord` — locates a patient and appends a diagnosis/treatment note.
- `FindPatientIndex` — reusable sequential-search function.
- `ValidatePatientInput` — prevents blank IDs, impossible ages, and empty names.

## Pseudocode
START

 CONSTANT MAX = 100

 MODULE Main()
    DECLARE INTEGER choice, count = 0, running = TRUE
    DECLARE ID[100], name[100], age[100], gender[100], phone[100], history[100]
    WHILE running == TRUE
        PRINT "1.Register 2.Search 3.Update 4.Exit"
        INPUT choice
        IF choice == 1 THEN
            IF count >= MAX THEN PRINT "Full"
            ELSE
                INPUT ID[count], name[count], age[count], gender[count], phone[count], history[count]
                IF age[count] < 0 OR age[count] > 130 THEN PRINT "Invalid Age"
                ELSE
                    SET count = count + 1
                    PRINT "Saved"
                END IF
            END IF
      
        ELSE IF choice == 2 THEN
            DECLARE target, pos = -1
            INPUT target
            FOR i = 0 TO count - 1
                IF ID[i] == target THEN SET pos = i
            END FOR
            IF pos == -1 THEN PRINT "Not Found"
            ELSE PRINT name[pos], age[pos], gender[pos], phone[pos], history[pos]
            END IF
        ELSE IF choice == 3 THEN
            DECLARE target, entry, pos = -1
            INPUT target, entry
            FOR i = 0 TO count - 1
                IF ID[i] == target THEN SET pos = i
            END FOR
            IF pos == -1 THEN PRINT "Not Found"
            ELSE 
                SET history[pos] = history[pos] + " | " + entry
                PRINT "Updated"
            END IF
        ELSE IF choice == 4 THEN
            SET running = FALSE
        END IF
    END WHILE
END MODULE
END


## Structure of the Flowchart 

<img width="943" height="1024" alt="image_84485a4b-2e61-4c58-9bcb-0b600e5ef2aa" src="https://github.com/user-attachments/assets/a4ff7c6f-7f15-46eb-901e-52ab8caeac42" />

