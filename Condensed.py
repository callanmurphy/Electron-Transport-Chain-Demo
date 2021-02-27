first = [nadh, fadh2]
    second = [nad, fad]
    value1 = [-30, -80]
    value2 = [20, 240]
    image1 = [nadhImage, fadh2Image]
    image2 = [nadImage, fadImage]
    move1 = [nadhMove1, fadh2Move1]
    move2 = [nadhMove2, fadh2Move2]
    h = [h1, h2]

    for k in range(0,len(first)):
        if len(first[k]) == 0:
            first[k].append(image1[k].get_rect())
            first[k][-1].centerx = -30
            first[k][-1].centery = 600
            move1[k] = True

        if len(first[k]) > 0:
            if move1[k] == True:
                first[k][-1].centerx += 2
            if first[k][-1].centerx == 20:
                move1[k] = False
                move2[k]= True
            if move2[k] == True:
                first[k][-1].centery -= 2
                first[k][-1].centerx += 2
            if first[k][-1].centery == 430:
                move2[k] = False
                second[k].append(image2[k].get_rect())
                second[k][-1].centerx = first[k][-1].centerx
                second[k][-1].centery = first[k][-1].centery
                h[k].append(hImage.get_rect())
                h[k][-1].centerx = first[k][-1].centerx + 60
                h[k][-1].centery = first[k][-1].centery
                if k == 1:
                    h2.append(hImage.get_rect())
                    h2[-2].centerx = fadh2[-1].centerx + 90
                    h2[-2].centery = fadh2[-1].centery
                first[k].pop(-1)

        if len(second[k]) > 0:
            for i in range(0, len(second[k])):
                second[k][i].centery += 2
                second[k][i].centerx += 2
                if second[k][i].centery == 725:
                    second[k].pop(i)
