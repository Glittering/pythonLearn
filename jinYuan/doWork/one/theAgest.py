if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    for key in person.keys():
        if person[key] == person[m]:
            print '%s,%d' % (key, person[key])


#problem age is same