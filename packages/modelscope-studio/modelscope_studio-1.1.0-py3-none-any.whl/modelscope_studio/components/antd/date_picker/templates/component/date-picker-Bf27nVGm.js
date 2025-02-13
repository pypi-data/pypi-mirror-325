import { i as Re, a as G, r as ke, g as je, w as N, b as Se } from "./Index-CeXfR8VB.js";
const S = window.ms_globals.React, Ie = window.ms_globals.React.forwardRef, we = window.ms_globals.React.useRef, Ee = window.ms_globals.React.useState, Ce = window.ms_globals.React.useEffect, E = window.ms_globals.React.useMemo, z = window.ms_globals.ReactDOM.createPortal, Oe = window.ms_globals.internalContext.useContextPropsContext, M = window.ms_globals.internalContext.ContextPropsProvider, Pe = window.ms_globals.antd.DatePicker, Y = window.ms_globals.dayjs, Te = window.ms_globals.createItemsContext.createItemsContext;
var Fe = /\s/;
function De(e) {
  for (var t = e.length; t-- && Fe.test(e.charAt(t)); )
    ;
  return t;
}
var Le = /^\s+/;
function Ne(e) {
  return e && e.slice(0, De(e) + 1).replace(Le, "");
}
var K = NaN, Ae = /^[-+]0x[0-9a-f]+$/i, We = /^0b[01]+$/i, Me = /^0o[0-7]+$/i, Ue = parseInt;
function Q(e) {
  if (typeof e == "number")
    return e;
  if (Re(e))
    return K;
  if (G(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = G(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ne(e);
  var s = We.test(e);
  return s || Me.test(e) ? Ue(e.slice(2), s ? 2 : 8) : Ae.test(e) ? K : +e;
}
var V = function() {
  return ke.Date.now();
}, Ve = "Expected a function", Be = Math.max, He = Math.min;
function ze(e, t, s) {
  var l, o, n, r, i, u, x = 0, _ = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ve);
  t = Q(t) || 0, G(s) && (_ = !!s.leading, c = "maxWait" in s, n = c ? Be(Q(s.maxWait) || 0, t) : n, g = "trailing" in s ? !!s.trailing : g);
  function f(p) {
    var I = l, j = o;
    return l = o = void 0, x = p, r = e.apply(j, I), r;
  }
  function b(p) {
    return x = p, i = setTimeout(h, t), _ ? f(p) : r;
  }
  function d(p) {
    var I = p - u, j = p - x, D = t - I;
    return c ? He(D, n - j) : D;
  }
  function m(p) {
    var I = p - u, j = p - x;
    return u === void 0 || I >= t || I < 0 || c && j >= n;
  }
  function h() {
    var p = V();
    if (m(p))
      return y(p);
    i = setTimeout(h, d(p));
  }
  function y(p) {
    return i = void 0, g && l ? f(p) : (l = o = void 0, r);
  }
  function R() {
    i !== void 0 && clearTimeout(i), x = 0, l = u = o = i = void 0;
  }
  function a() {
    return i === void 0 ? r : y(V());
  }
  function k() {
    var p = V(), I = m(p);
    if (l = arguments, o = this, u = p, I) {
      if (i === void 0)
        return b(u);
      if (c)
        return clearTimeout(i), i = setTimeout(h, t), f(u);
    }
    return i === void 0 && (i = setTimeout(h, t)), r;
  }
  return k.cancel = R, k.flush = a, k;
}
var ce = {
  exports: {}
}, U = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ge = S, qe = Symbol.for("react.element"), Je = Symbol.for("react.fragment"), Xe = Object.prototype.hasOwnProperty, Ye = Ge.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ke = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ae(e, t, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Xe.call(t, l) && !Ke.hasOwnProperty(l) && (o[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: qe,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Ye.current
  };
}
U.Fragment = Je;
U.jsx = ae;
U.jsxs = ae;
ce.exports = U;
var v = ce.exports;
const {
  SvelteComponent: Qe,
  assign: Z,
  binding_callbacks: $,
  check_outros: Ze,
  children: ue,
  claim_element: fe,
  claim_space: $e,
  component_subscribe: ee,
  compute_slots: et,
  create_slot: tt,
  detach: T,
  element: de,
  empty: te,
  exclude_internal_props: ne,
  get_all_dirty_from_scope: nt,
  get_slot_changes: rt,
  group_outros: ot,
  init: st,
  insert_hydration: A,
  safe_not_equal: lt,
  set_custom_element_data: me,
  space: it,
  transition_in: W,
  transition_out: q,
  update_slot_base: ct
} = window.__gradio__svelte__internal, {
  beforeUpdate: at,
  getContext: ut,
  onDestroy: ft,
  setContext: dt
} = window.__gradio__svelte__internal;
function re(e) {
  let t, s;
  const l = (
    /*#slots*/
    e[7].default
  ), o = tt(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = de("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = fe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ue(t);
      o && o.l(r), r.forEach(T), this.h();
    },
    h() {
      me(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      A(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && ct(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? rt(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : nt(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (W(o, n), s = !0);
    },
    o(n) {
      q(o, n), s = !1;
    },
    d(n) {
      n && T(t), o && o.d(n), e[9](null);
    }
  };
}
function mt(e) {
  let t, s, l, o, n = (
    /*$$slots*/
    e[4].default && re(e)
  );
  return {
    c() {
      t = de("react-portal-target"), s = it(), n && n.c(), l = te(), this.h();
    },
    l(r) {
      t = fe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ue(t).forEach(T), s = $e(r), n && n.l(r), l = te(), this.h();
    },
    h() {
      me(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      A(r, t, i), e[8](t), A(r, s, i), n && n.m(r, i), A(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && W(n, 1)) : (n = re(r), n.c(), W(n, 1), n.m(l.parentNode, l)) : n && (ot(), q(n, 1, 1, () => {
        n = null;
      }), Ze());
    },
    i(r) {
      o || (W(n), o = !0);
    },
    o(r) {
      q(n), o = !1;
    },
    d(r) {
      r && (T(t), T(s), T(l)), e[8](null), n && n.d(r);
    }
  };
}
function oe(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function pt(e, t, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = et(n);
  let {
    svelteInit: u
  } = t;
  const x = N(oe(t)), _ = N();
  ee(e, _, (a) => s(0, l = a));
  const c = N();
  ee(e, c, (a) => s(1, o = a));
  const g = [], f = ut("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: d,
    subSlotIndex: m
  } = je() || {}, h = u({
    parent: f,
    props: x,
    target: _,
    slot: c,
    slotKey: b,
    slotIndex: d,
    subSlotIndex: m,
    onDestroy(a) {
      g.push(a);
    }
  });
  dt("$$ms-gr-react-wrapper", h), at(() => {
    x.set(oe(t));
  }), ft(() => {
    g.forEach((a) => a());
  });
  function y(a) {
    $[a ? "unshift" : "push"](() => {
      l = a, _.set(l);
    });
  }
  function R(a) {
    $[a ? "unshift" : "push"](() => {
      o = a, c.set(o);
    });
  }
  return e.$$set = (a) => {
    s(17, t = Z(Z({}, t), ne(a))), "svelteInit" in a && s(5, u = a.svelteInit), "$$scope" in a && s(6, r = a.$$scope);
  }, t = ne(t), [l, o, _, c, i, u, r, n, y, R];
}
class _t extends Qe {
  constructor(t) {
    super(), st(this, t, pt, mt, lt, {
      svelteInit: 5
    });
  }
}
const se = window.ms_globals.rerender, B = window.ms_globals.tree;
function ht(e, t = {}) {
  function s(l) {
    const o = N(), n = new _t({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? B;
          return u.nodes = [...u.nodes, i], se({
            createPortal: z,
            node: B
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((x) => x.svelteInstance !== o), se({
              createPortal: z,
              node: B
            });
          }), i;
        },
        ...l.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(s);
    });
  });
}
const xt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function gt(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const l = e[s];
    return t[s] = vt(s, l), t;
  }, {}) : {};
}
function vt(e, t) {
  return typeof t == "number" && !xt.includes(e) ? t + "px" : t;
}
function J(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = S.Children.toArray(e._reactElement.props.children).map((n) => {
      if (S.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = J(n.props.el);
        return S.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...S.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(z(S.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: u
    }) => {
      s.addEventListener(i, r, u);
    });
  });
  const l = Array.from(e.childNodes);
  for (let o = 0; o < l.length; o++) {
    const n = l[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = J(n);
      t.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function bt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const w = Ie(({
  slot: e,
  clone: t,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = we(), [i, u] = Ee([]), {
    forceClone: x
  } = Oe(), _ = x ? !0 : t;
  return Ce(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function g() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), bt(n, d), s && d.classList.add(...s.split(" ")), l) {
        const m = gt(l);
        Object.keys(m).forEach((h) => {
          d.style[h] = m[h];
        });
      }
    }
    let f = null;
    if (_ && window.MutationObserver) {
      let d = function() {
        var R, a, k;
        (R = r.current) != null && R.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: y
        } = J(e);
        c = y, u(h), c.style.display = "contents", g(), (k = r.current) == null || k.appendChild(c);
      };
      d();
      const m = ze(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      f = new window.MutationObserver(m), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var d, m;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((m = r.current) == null || m.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, _, s, l, n, o]), S.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function yt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function It(e, t = !1) {
  try {
    if (Se(e))
      return e;
    if (t && !yt(e))
      return;
    if (typeof e == "string") {
      let s = e.trim();
      return s.startsWith(";") && (s = s.slice(1)), s.endsWith(";") && (s = s.slice(0, -1)), new Function(`return (...args) => (${s})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function F(e, t) {
  return E(() => It(e, t), [e, t]);
}
function pe(e, t, s) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((o, n) => {
      var x;
      if (typeof o != "object")
        return o;
      const r = {
        ...o.props,
        key: ((x = o.props) == null ? void 0 : x.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((_) => {
        if (!o.slots[_] || !(o.slots[_] instanceof Element) && !o.slots[_].el)
          return;
        const c = _.split(".");
        c.forEach((h, y) => {
          i[h] || (i[h] = {}), y !== c.length - 1 && (i = r[h]);
        });
        const g = o.slots[_];
        let f, b, d = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? f = g : (f = g.el, b = g.callback, d = g.clone ?? d, m = g.forceClone ?? m), m = m ?? !!b, i[c[c.length - 1]] = f ? b ? (...h) => (b(c[c.length - 1], h), /* @__PURE__ */ v.jsx(M, {
          params: h,
          forceClone: m,
          children: /* @__PURE__ */ v.jsx(w, {
            slot: f,
            clone: d
          })
        })) : /* @__PURE__ */ v.jsx(M, {
          forceClone: m,
          children: /* @__PURE__ */ v.jsx(w, {
            slot: f,
            clone: d
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const u = "children";
      return o[u] && (r[u] = pe(o[u], t, `${n}`)), r;
    });
}
function le(e, t) {
  return e ? /* @__PURE__ */ v.jsx(w, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function H({
  key: e,
  slots: t,
  targets: s
}, l) {
  return t[e] ? (...o) => s ? s.map((n, r) => /* @__PURE__ */ v.jsx(M, {
    params: o,
    forceClone: !0,
    children: le(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ v.jsx(M, {
    params: o,
    forceClone: !0,
    children: le(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  withItemsContextProvider: wt,
  useItems: Et,
  ItemHandler: Rt
} = Te("antd-date-picker-presets");
function C(e) {
  return Array.isArray(e) ? e.map((t) => C(t)) : Y(typeof e == "number" ? e * 1e3 : e);
}
function ie(e) {
  return Array.isArray(e) ? e.map((t) => t ? t.valueOf() / 1e3 : null) : typeof e == "object" && e !== null ? e.valueOf() / 1e3 : e;
}
const kt = ht(wt(["presets"], ({
  slots: e,
  disabledDate: t,
  disabledTime: s,
  value: l,
  defaultValue: o,
  defaultPickerValue: n,
  pickerValue: r,
  showTime: i,
  presets: u,
  onChange: x,
  minDate: _,
  maxDate: c,
  cellRender: g,
  panelRender: f,
  getPopupContainer: b,
  onValueChange: d,
  onPanelChange: m,
  children: h,
  setSlotParams: y,
  elRef: R,
  ...a
}) => {
  const k = F(t), p = F(s), I = F(b), j = F(g), D = F(f), _e = E(() => typeof i == "object" ? {
    ...i,
    defaultValue: i.defaultValue ? C(i.defaultValue) : void 0
  } : i, [i]), he = E(() => l ? C(l) : void 0, [l]), xe = E(() => o ? C(o) : void 0, [o]), ge = E(() => n ? C(n) : void 0, [n]), ve = E(() => r ? C(r) : void 0, [r]), be = E(() => _ ? C(_) : void 0, [_]), ye = E(() => c ? C(c) : void 0, [c]), {
    items: {
      presets: X
    }
  } = Et();
  return /* @__PURE__ */ v.jsxs(v.Fragment, {
    children: [/* @__PURE__ */ v.jsx("div", {
      style: {
        display: "none"
      },
      children: h
    }), /* @__PURE__ */ v.jsx(Pe, {
      ...a,
      ref: R,
      value: he,
      defaultValue: xe,
      defaultPickerValue: ge,
      pickerValue: ve,
      minDate: be,
      maxDate: ye,
      showTime: _e,
      disabledDate: k,
      disabledTime: p,
      getPopupContainer: I,
      cellRender: e.cellRender ? H({
        slots: e,
        setSlotParams: y,
        key: "cellRender"
      }) : j,
      panelRender: e.panelRender ? H({
        slots: e,
        setSlotParams: y,
        key: "panelRender"
      }) : D,
      presets: E(() => {
        var O;
        return (O = u || pe(X)) == null ? void 0 : O.map((P) => ({
          ...P,
          value: C(P.value)
        }));
      }, [u, X]),
      onPanelChange: (O, ...P) => {
        const L = ie(O);
        m == null || m(L, ...P);
      },
      onChange: (O, ...P) => {
        const L = ie(O);
        x == null || x(L, ...P), d(L);
      },
      renderExtraFooter: e.renderExtraFooter ? H({
        slots: e,
        setSlotParams: y,
        key: "renderExtraFooter"
      }) : a.renderExtraFooter,
      prevIcon: e.prevIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.prevIcon
      }) : a.prevIcon,
      prefix: e.prefix ? /* @__PURE__ */ v.jsx(w, {
        slot: e.prefix
      }) : a.prefix,
      nextIcon: e.nextIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.nextIcon
      }) : a.nextIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.suffixIcon
      }) : a.suffixIcon,
      superNextIcon: e.superNextIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.superNextIcon
      }) : a.superNextIcon,
      superPrevIcon: e.superPrevIcon ? /* @__PURE__ */ v.jsx(w, {
        slot: e.superPrevIcon
      }) : a.superPrevIcon,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ v.jsx(w, {
          slot: e["allowClear.clearIcon"]
        })
      } : a.allowClear
    })]
  });
}));
export {
  kt as DatePicker,
  kt as default
};
